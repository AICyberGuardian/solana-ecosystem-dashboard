from typing import Dict, Any

class HealthScoreEngine:
    """Computes a deterministic 0-100 Ecosystem Health Score across 4 core operational pillars."""

    def compute(self, telemetry: Dict[str, Any]) -> Dict[str, Any]:
        network = telemetry.get("network", {})
        validators = telemetry.get("validators", {})
        defi = telemetry.get("defi", {})
        tvl_data = defi.get("tvl", {})
        dex_data = defi.get("dex", {})
        stable_data = defi.get("stablecoins", {})

        # --- 1. Network Liveness (25 points) ---
        liveness_score = 0.0
        health = network.get("health", "unknown")
        if health == "ok":
            liveness_score += 15.0
        elif health == "behind":
            liveness_score += 8.0

        slot_time = network.get("current_slot_time_ms", 400.0)
        if slot_time <= 420.0:
            liveness_score += 10.0
        elif slot_time <= 480.0:
            liveness_score += 7.0
        elif slot_time <= 550.0:
            liveness_score += 4.0

        # --- 2. Throughput & Stability (25 points) ---
        throughput_score = 0.0
        tps = network.get("current_tps", 0.0)
        if tps >= 3500:
            throughput_score += 15.0
        elif tps >= 2500:
            throughput_score += 12.0
        elif tps >= 1500:
            throughput_score += 8.0
        elif tps >= 500:
            throughput_score += 4.0

        avg_tps = network.get("avg_tps_1h", 0.0)
        if avg_tps > 0:
            dev = abs(tps - avg_tps) / avg_tps
            if dev <= 0.20:
                throughput_score += 10.0
            elif dev <= 0.40:
                throughput_score += 6.0
            else:
                throughput_score += 3.0
        else:
            throughput_score += 5.0

        # --- 3. Decentralization & Security (25 points) ---
        security_score = 0.0
        nakamoto = validators.get("nakamoto_coefficient", 19)
        if nakamoto >= 18:
            security_score += 15.0
        elif nakamoto >= 16:
            security_score += 12.0
        elif nakamoto >= 14:
            security_score += 8.0
        else:
            security_score += 4.0

        delinquency_rate = validators.get("delinquency_rate_pct", 0.0)
        if delinquency_rate < 2.0:
            security_score += 10.0
        elif delinquency_rate < 4.0:
            security_score += 7.0
        elif delinquency_rate < 6.0:
            security_score += 4.0

        # --- 4. DeFi & Economic Vitality (25 points) ---
        economic_score = 0.0
        tvl = tvl_data.get("current_tvl_usd", 0.0)
        if tvl >= 5_000_000_000:
            economic_score += 10.0
        elif tvl >= 3_000_000_000:
            economic_score += 7.0
        elif tvl >= 1_000_000_000:
            economic_score += 4.0

        stables = stable_data.get("total_stablecoins_usd", 0.0)
        if stables >= 10_000_000_000:
            economic_score += 10.0
        elif stables >= 5_000_000_000:
            economic_score += 7.0
        elif stables >= 2_000_000_000:
            economic_score += 4.0

        dex_vol = dex_data.get("dex_volume_24h_usd", 0.0)
        if dex_vol >= 1_000_000_000:
            economic_score += 5.0
        elif dex_vol >= 500_000_000:
            economic_score += 3.0

        # Total Composite Score
        total_score = round(liveness_score + throughput_score + security_score + economic_score, 1)

        if total_score >= 90.0:
            status = "OPTIMAL"
            color = "#14F195" # Solana green
        elif total_score >= 75.0:
            status = "HEALTHY"
            color = "#00FFA3"
        elif total_score >= 60.0:
            status = "MODERATE"
            color = "#FFA500"
        else:
            status = "DEGRADED"
            color = "#FF4444"

        return {
            "score": total_score,
            "status": status,
            "color": color,
            "pillars": {
                "liveness": round(liveness_score, 1),
                "throughput": round(throughput_score, 1),
                "security": round(security_score, 1),
                "economic": round(economic_score, 1)
            }
        }
