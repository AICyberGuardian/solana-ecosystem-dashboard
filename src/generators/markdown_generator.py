from pathlib import Path
from typing import Dict, Any, List

class MarkdownGenerator:
    """Generates an executive-ready Markdown status report following strict technical prose standards."""

    def __init__(self, output_path: str = "output/report.md"):
        self.output_path = Path(output_path)

    def generate(self, data: Dict[str, Any]) -> str:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        meta = data.get("meta", {})
        network = data.get("network", {})
        validators = data.get("validators", {})
        supply = data.get("supply", {})
        defi = data.get("defi", {})
        tvl = defi.get("tvl", {})
        dex = defi.get("dex", {})
        stables = defi.get("stablecoins", {})
        market = data.get("market", {})
        health = data.get("health_score", {})
        anomalies = data.get("anomalies", [])

        ts = meta.get("generated_at_utc", "N/A")
        score = health.get("score", 0.0)
        status = health.get("status", "UNKNOWN")

        lines = [
            "# Solana Ecosystem Status & Telemetry Report",
            f"**Generated:** `{ts}` | **Health Score:** `{score}/100` ({status}) | **Zero API Keys**",
            "",
            "---",
            "",
            "## 1. Executive Summary",
            "",
            f"The Solana mainnet cluster is operating under **{status}** parameters with a composite health rating of **{score}/100**.",
            f"Current network throughput stands at **{network.get('current_tps', 0.0):,.1f} TPS** (1-hour average: {network.get('avg_tps_1h', 0.0):,.1f} TPS) with an average slot generation interval of **{network.get('avg_slot_time_ms', 400.0):.1f} ms**.",
            f"Total value locked across Solana DeFi protocols totals **${tvl.get('current_tvl_usd', 0.0) / 1e9:.2f}B** ({tvl.get('tvl_change_24h_pct', 0.0):+.2f}% 24h delta), backed by **${stables.get('total_stablecoins_usd', 0.0) / 1e9:.2f}B** in on-chain stablecoin liquidity.",
            "",
            "---",
            "",
            "## 2. Network Performance & Consensus",
            "",
            "| Metric | Current Value | Baseline / Target | Status |",
            "| :--- | :--- | :--- | :--- |",
            f"| Cluster Health | `{network.get('health', 'unknown')}` | `ok` | {'Normal' if network.get('health') == 'ok' else 'Alert'} |",
            f"| Current Slot | `{network.get('current_slot', 0):,}` | N/A | Active |",
            f"| Block Height | `{network.get('block_height', 0):,}` | N/A | Active |",
            f"| Current Epoch | `{network.get('epoch', 0)}` ({network.get('epoch_progress_pct', 0.0)}% complete) | 432,000 slots | In Progress |",
            f"| Throughput (Current) | `{network.get('current_tps', 0.0):,.1f} TPS` | > 2,500 TPS | Healthy |",
            f"| Throughput (1h Peak / Min) | `{network.get('peak_tps_1h', 0.0):,.1f}` / `{network.get('min_tps_1h', 0.0):,.1f} TPS` | N/A | Measured |",
            f"| Slot Duration | `{network.get('current_slot_time_ms', 0.0):.1f} ms` | ~400.0 ms | {'Normal' if network.get('current_slot_time_ms', 0) < 550 else 'High'} |",
            f"| Total Transactions | `{network.get('total_transaction_count', 0):,}` | Monotonic | Active |",
            "",
            "---",
            "",
            "## 3. Validator Health & Decentralization",
            "",
            "- **Active Validators:** " + f"{validators.get('active_validators', 0):,} nodes",
            "- **Delinquent Validators:** " + f"{validators.get('delinquent_validators', 0):,} nodes ({validators.get('delinquency_rate_pct', 0.0):.2f}% delinquency rate)",
            "- **Total Active Stake:** " + f"{validators.get('total_active_stake_sol', 0.0):,.2f} SOL",
            "- **Nakamoto Coefficient:** " + f"`{validators.get('nakamoto_coefficient', 0)}` minimum validators required to compromise consensus (>33.33% total active stake)",
            "",
            "### Top 5 Validators by Active Stake",
            "",
            "| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |",
            "| :--- | :--- | :--- | :--- | :--- |"
        ]

        top_vals = validators.get("top_10_validators", [])[:5]
        for v in top_vals:
            vote_short = v.get("vote_pubkey", "")[:8] + "..." + v.get("vote_pubkey", "")[-6:]
            lines.append(f"| #{v.get('rank')} | `{vote_short}` | {v.get('stake_sol', 0.0):,.1f} SOL | {v.get('stake_share_pct', 0.0):.2f}% | {v.get('commission', 0)}% |")

        lines.extend([
            "",
            "---",
            "",
            "## 4. Economic Indicators & DeFi Metrics",
            "",
            "| Indicator | Value (USD) | 24h Change / Details |",
            "| :--- | :--- | :--- |",
            f"| SOL Spot Price | `${market.get('price_usd', 0.0):,.2f}` | {market.get('change_24h_pct', 0.0):+.2f}% (Source: {market.get('source', 'Public API')}) |",
            f"| Estimated Circulating Market Cap | `${market.get('market_cap_usd_est', 0.0) / 1e9:.2f}B` | {supply.get('circulating_supply_sol', 0.0) / 1e6:.1f}M SOL circulating |",
            f"| 24h DEX Trading Volume | `${dex.get('dex_volume_24h_usd', 0.0) / 1e9:.2f}B` | {dex.get('dex_volume_change_24h_pct', 0.0):+.2f}% delta |",
            f"| Total DeFi TVL | `${tvl.get('current_tvl_usd', 0.0) / 1e9:.2f}B` | {tvl.get('tvl_change_24h_pct', 0.0):+.2f}% delta |",
            f"| Circulating Stablecoins | `${stables.get('total_stablecoins_usd', 0.0) / 1e9:.2f}B` | USD: ${stables.get('usd_pegged_stables', 0.0)/1e9:.2f}B, CAD: ${stables.get('cad_pegged_stables', 0.0):,.0f} |",
            f"| Median Transaction Fee | `${market.get('median_tx_fee_usd', 0.0):.5f}` | ~{market.get('median_tx_fee_sol', 0.0):.6f} SOL |",
            "",
            "---",
            "",
            "## 5. Anomaly Detection Feed",
            ""
        ])

        if not anomalies:
            lines.append("✅ **All Systems Nominal.** Zero telemetry anomalies detected across latency, throughput, validator delinquency, TVL, and spot price bounds.")
        else:
            lines.append("| Severity | Metric | Current Value | Threshold | Details |")
            lines.append("| :--- | :--- | :--- | :--- | :--- |")
            for a in anomalies:
                lines.append(f"| `{a.get('severity')}` | **{a.get('metric')}** | `{a.get('current_value')}` | `{a.get('expected')}` | {a.get('message')} |")

        lines.extend([
            "",
            "---",
            "",
            "## 6. Architecture & Data Provenance",
            "",
            "- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).",
            "- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.",
            "- **Market Data:** Public Binance & Coinbase spot ticker endpoints.",
            "- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.",
            ""
        ])

        content = "\n".join(lines)
        self.output_path.write_text(content, encoding="utf-8")
        return str(self.output_path)
