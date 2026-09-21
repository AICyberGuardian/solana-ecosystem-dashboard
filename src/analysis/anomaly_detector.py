from typing import Dict, Any, List
import math
import statistics

def calculate_mad(values: List[float]) -> float:
    """Calculates Median Absolute Deviation scaled by 1.4826 for normal consistency (Bruce & Gedeck)."""
    if not values or len(values) < 2:
        return 0.0
    med = statistics.median(values)
    abs_devs = [abs(x - med) for x in values]
    return round(1.4826 * statistics.median(abs_devs), 3)

class AnomalyDetector:
    """Detects statistical anomalies and operational degradation across Solana telemetry metrics using robust statistics."""

    def __init__(self,
                 tps_drop_threshold_pct: float = 25.0,
                 slot_time_max_ms: float = 550.0,
                 delinquency_max_pct: float = 5.0,
                 tvl_change_max_pct: float = 10.0,
                 price_change_max_pct: float = 12.0,
                 mad_outlier_threshold: float = 3.0):
        self.tps_drop_threshold_pct = tps_drop_threshold_pct
        self.slot_time_max_ms = slot_time_max_ms
        self.delinquency_max_pct = delinquency_max_pct
        self.tvl_change_max_pct = tvl_change_max_pct
        self.price_change_max_pct = price_change_max_pct
        self.mad_outlier_threshold = mad_outlier_threshold

    def analyze(self, telemetry: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Scans combined telemetry data and flags anomalies with severity levels."""
        anomalies = []

        network = telemetry.get("network", {})
        validators = telemetry.get("validators", {})
        tvl_data = telemetry.get("defi", {}).get("tvl", {})
        market = telemetry.get("market", {})

        # 1. RPC Health Check
        health = network.get("health", "unknown")
        if health != "ok":
            anomalies.append({
                "metric": "Network Node Health",
                "severity": "CRITICAL" if health == "degraded" else "WARNING",
                "current_value": health,
                "expected": "ok",
                "message": f"Solana cluster RPC node reported health status '{health}'."
            })

        # 2. TPS Drop / Surge Check
        current_tps = network.get("current_tps", 0.0)
        avg_tps = network.get("avg_tps_1h", 0.0)
        if avg_tps > 0 and current_tps > 0:
            delta_pct = ((current_tps - avg_tps) / avg_tps) * 100
            if delta_pct < -self.tps_drop_threshold_pct:
                anomalies.append({
                    "metric": "Transaction Throughput (TPS)",
                    "severity": "WARNING",
                    "current_value": f"{current_tps:.1f} TPS",
                    "expected": f"~{avg_tps:.1f} TPS",
                    "message": f"Current throughput is {abs(delta_pct):.1f}% below 1-hour average."
                })
            elif delta_pct > 60.0:
                anomalies.append({
                    "metric": "Transaction Throughput (TPS)",
                    "severity": "INFO",
                    "current_value": f"{current_tps:.1f} TPS",
                    "expected": f"~{avg_tps:.1f} TPS",
                    "message": f"Throughput spike detected: {delta_pct:.1f}% above 1-hour baseline."
                })

        # Statistical outlier detection via 1.4826 MAD factor on TPS series
        tps_history = network.get("tps_history", [])
        if len(tps_history) >= 10 and current_tps > 0:
            mad_val = calculate_mad(tps_history)
            med_val = statistics.median(tps_history)
            if mad_val > 0:
                mod_z = abs(current_tps - med_val) / mad_val
                if mod_z > self.mad_outlier_threshold and not any(a["metric"].startswith("Transaction Throughput") for a in anomalies):
                    anomalies.append({
                        "metric": "Transaction Throughput (MAD Outlier)",
                        "severity": "WARNING" if current_tps < med_val else "INFO",
                        "current_value": f"{current_tps:.1f} TPS",
                        "expected": f"Median {med_val:.1f} ± {mad_val:.1f} MAD",
                        "message": f"Throughput deviates by {mod_z:.1f}x MAD from rolling median."
                    })

        # 3. Slot Time Latency Check
        current_slot_time = network.get("current_slot_time_ms", 400.0)
        if current_slot_time > self.slot_time_max_ms:
            anomalies.append({
                "metric": "Slot Duration",
                "severity": "WARNING" if current_slot_time < 700.0 else "CRITICAL",
                "current_value": f"{current_slot_time:.1f} ms",
                "expected": "<= 450.0 ms",
                "message": f"Slot generation latency elevated to {current_slot_time:.1f} ms (normal target: 400 ms)."
            })

        # 4. Validator Delinquency Check
        delinquency_pct = validators.get("delinquency_rate_pct", 0.0)
        if delinquency_pct > self.delinquency_max_pct:
            anomalies.append({
                "metric": "Validator Delinquency Rate",
                "severity": "WARNING" if delinquency_pct < 10.0 else "CRITICAL",
                "current_value": f"{delinquency_pct:.2f}%",
                "expected": f"<= {self.delinquency_max_pct}%",
                "message": f"{delinquency_pct:.2f}% of validators are currently delinquent or missing votes."
            })

        # 5. Nakamoto Coefficient Threshold
        nakamoto = validators.get("nakamoto_coefficient", 19)
        if nakamoto < 16:
            anomalies.append({
                "metric": "Nakamoto Coefficient",
                "severity": "WARNING",
                "current_value": str(nakamoto),
                "expected": ">= 18",
                "message": f"Decentralization coefficient dipped to {nakamoto} validators."
            })

        # 6. TVL Volatility Check
        tvl_change_24h = tvl_data.get("tvl_change_24h_pct", 0.0)
        if abs(tvl_change_24h) > self.tvl_change_max_pct:
            anomalies.append({
                "metric": "DeFi TVL (24h Delta)",
                "severity": "INFO" if tvl_change_24h > 0 else "WARNING",
                "current_value": f"{tvl_change_24h:+.2f}%",
                "expected": f"Within ±{self.tvl_change_max_pct}%",
                "message": f"Large TVL swing of {tvl_change_24h:+.2f}% observed across Solana protocols in 24 hours."
            })

        # 7. SOL Spot Price Volatility Check
        price_change_24h = market.get("change_24h_pct", 0.0)
        if abs(price_change_24h) > self.price_change_max_pct:
            anomalies.append({
                "metric": "SOL Spot Price (24h Delta)",
                "severity": "INFO" if price_change_24h > 0 else "WARNING",
                "current_value": f"{price_change_24h:+.2f}%",
                "expected": f"Within ±{self.price_change_max_pct}%",
                "message": f"Elevated market volatility: SOL price moved {price_change_24h:+.2f}% in 24 hours."
            })

        return anomalies
