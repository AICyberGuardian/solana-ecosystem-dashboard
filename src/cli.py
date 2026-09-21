import argparse
import sys
import time
import http.server
import socketserver
import threading
from pathlib import Path
from typing import Dict, Any, Optional

from .config import (
    DEFAULT_PUBLIC_RPCS,
    DEFAULT_OUTPUT_DIR,
    DEFAULT_JSON_OUTPUT,
    DEFAULT_MD_OUTPUT,
    DEFAULT_HTML_OUTPUT,
    DEFAULT_REFRESH_INTERVAL_SEC,
    DEFAULT_HTTP_PORT,
    DEFAULT_TIMEOUT_SEC
)
from .collectors import SolanaRPCCollector, DeFiLlamaCollector, MarketCollector
from .analysis import AnomalyDetector, HealthScoreEngine
from .generators import JSONGenerator, MarkdownGenerator, HTMLGenerator

class DashboardOrchestrator:
    """Coordinates telemetry collection, anomaly detection, health scoring, and output generation."""

    def __init__(self, rpc_urls: Optional[list] = None, timeout: int = DEFAULT_TIMEOUT_SEC):
        self.rpc_collector = SolanaRPCCollector(rpc_urls=rpc_urls or DEFAULT_PUBLIC_RPCS, timeout=timeout)
        self.defillama_collector = DeFiLlamaCollector(timeout=timeout)
        self.market_collector = MarketCollector(timeout=timeout)
        self.anomaly_detector = AnomalyDetector()
        self.health_engine = HealthScoreEngine()
        self.json_gen = JSONGenerator(DEFAULT_JSON_OUTPUT)
        self.md_gen = MarkdownGenerator(DEFAULT_MD_OUTPUT)
        self.html_gen = HTMLGenerator(output_path=DEFAULT_HTML_OUTPUT)

    def execute_cycle(self) -> Dict[str, Any]:
        """Runs a single pass of data collection and report generation."""
        print("[*] Fetching live Solana on-chain telemetry from public RPCs...")
        rpc_data = self.rpc_collector.collect_all()

        print("[*] Fetching DeFi, TVL, and stablecoin metrics from DeFiLlama...")
        defi_data = self.defillama_collector.collect_all()

        print("[*] Fetching market prices and economic indicators...")
        circulating_sol = rpc_data.get("supply", {}).get("circulating_supply_sol", 468000000.0)
        market_data = self.market_collector.collect_market_data(circulating_supply_sol=circulating_sol)

        payload = {
            "meta": {
                "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "collector_version": "1.0.0",
                "cluster": "mainnet-beta"
            },
            "network": rpc_data.get("network", {}),
            "validators": rpc_data.get("validators", {}),
            "supply": rpc_data.get("supply", {}),
            "defi": defi_data,
            "market": market_data
        }

        print("[*] Evaluating health score and anomaly rules...")
        health_score = self.health_engine.compute(payload)
        anomalies = self.anomaly_detector.analyze(payload)

        payload["health_score"] = health_score
        payload["anomalies"] = anomalies

        print("[*] Generating output artifacts...")
        json_path = self.json_gen.generate(payload)
        md_path = self.md_gen.generate(payload)
        html_path = self.html_gen.generate(payload)

        print(f"[+] Successfully generated reports:")
        print(f"    - JSON:      {json_path}")
        print(f"    - Markdown:  {md_path}")
        print(f"    - Dashboard: {html_path}")
        print(f"[+] Health Score: {health_score['score']}/100 ({health_score['status']}) | Anomalies: {len(anomalies)}")

        return payload

def run_http_server(port: int = DEFAULT_HTTP_PORT):
    """Starts a lightweight static HTTP server serving the output directory."""
    out_dir = Path(DEFAULT_OUTPUT_DIR).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(out_dir), **kwargs)

        def log_message(self, format, *args):
            # Suppress routine GET logging to keep console clean
            pass

    with socketserver.TCPServer(("", port), QuietHandler) as httpd:
        print(f"\n🚀 Interactive Dashboard live at: http://localhost:{port}/dashboard.html")
        print("Press Ctrl+C to stop the server.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")

def main():
    parser = argparse.ArgumentParser(
        description="Solana Ecosystem Auto-Updating Report & Interactive Bento Dashboard",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--generate", action="store_true", help="Generate all reports once and exit")
    parser.add_argument("--daemon", action="store_true", help="Run background daemon auto-refreshing at interval")
    parser.add_argument("--interval", type=int, default=DEFAULT_REFRESH_INTERVAL_SEC, help="Refresh interval in seconds for daemon")
    parser.add_argument("--serve", action="store_true", help="Start local HTTP server to view interactive dashboard")
    parser.add_argument("--port", type=int, default=DEFAULT_HTTP_PORT, help="Port for local HTTP server")

    args = parser.parse_args()

    # Default action if no flags provided: generate reports once
    if not args.generate and not args.daemon and not args.serve:
        args.generate = True

    orchestrator = DashboardOrchestrator()

    if args.daemon:
        print(f"[*] Starting Solana Ecosystem daemon (interval: {args.interval}s)...")
        if args.serve:
            server_thread = threading.Thread(target=run_http_server, args=(args.port,), daemon=True)
            server_thread.start()

        try:
            while True:
                orchestrator.execute_cycle()
                print(f"[*] Sleeping for {args.interval} seconds... (Press Ctrl+C to terminate)")
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n[*] Daemon stopped by user.")
            sys.exit(0)

    elif args.serve:
        # Run one collection pass first to make sure files exist
        orchestrator.execute_cycle()
        run_http_server(args.port)

    elif args.generate:
        orchestrator.execute_cycle()

if __name__ == "__main__":
    main()
