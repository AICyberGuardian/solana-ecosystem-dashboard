import json
from pathlib import Path
from typing import Dict, Any, List

class HTMLGenerator:
    """Renders the self-contained interactive Bento UI HTML dashboard with zero external dependencies."""

    def __init__(self, template_path: str = "templates/dashboard.html", output_path: str = "output/dashboard.html"):
        self.template_path = Path(template_path)
        self.output_path = Path(output_path)

    def generate(self, data: Dict[str, Any]) -> str:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        template = self.template_path.read_text(encoding="utf-8")

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

        # Health dial dashoffset calculation (perimeter = 2 * pi * 42 ~= 264)
        score = health.get("score", 0.0)
        dashoffset = round(264.0 - (score / 100.0 * 264.0), 1)

        # Pillars % of max 25
        pillars = health.get("pillars", {})
        liveness_pct = min(100, round((pillars.get("liveness", 0) / 25.0) * 100))
        throughput_pct = min(100, round((pillars.get("throughput", 0) / 25.0) * 100))
        security_pct = min(100, round((pillars.get("security", 0) / 25.0) * 100))
        economic_pct = min(100, round((pillars.get("economic", 0) / 25.0) * 100))

        # TVL chart series
        history_30d = tvl.get("history_30d", [])
        tvl_labels = [pt.get("date", "") for pt in history_30d]
        tvl_values = [pt.get("tvl_usd", 0) for pt in history_30d]

        # Top protocols table rows
        protocols = defi.get("top_protocols", [])
        proto_rows = []
        for p in protocols:
            chg = p.get("change_1d", 0.0)
            chg_cls = "delta-up" if chg >= 0 else "delta-down"
            proto_rows.append(
                f"<tr>"
                f"<td><strong>{p.get('name')}</strong></td>"
                f"<td><span class='badge'>{p.get('category')}</span></td>"
                f"<td>${p.get('tvl_usd', 0) / 1e6:,.1f}M</td>"
                f"<td><span class='{chg_cls}'>{chg:+.2f}%</span></td>"
                f"</tr>"
            )
        protocols_table_rows = "\n".join(proto_rows) if proto_rows else "<tr><td colspan='4'>No protocols recorded</td></tr>"

        # Anomaly feed
        if not anomalies:
            anomaly_badge_text = "Nominal"
            anomaly_feed_html = (
                "<div style='display: flex; align-items: center; gap: 10px; padding: 14px; background: rgba(20, 241, 149, 0.05); border-radius: 10px; border: 1px solid rgba(20, 241, 149, 0.2);'>"
                "<span style='color: var(--solana-green); font-size: 1.2rem;'>✔</span>"
                "<span style='font-size: 0.85rem; color: #E5E7EB;'>All systems nominal. Zero anomalous deviations detected across TPS, slot times, or validator delinquency.</span>"
                "</div>"
            )
        else:
            anomaly_badge_text = f"{len(anomalies)} Alerts"
            items = []
            for a in anomalies:
                sev = a.get("severity", "INFO")
                items.append(
                    f"<div class='anomaly-item'>"
                    f"<div class='anomaly-icon {sev}'>{sev[0]}</div>"
                    f"<div class='anomaly-content'>"
                    f"<h4>{a.get('metric')} ({sev})</h4>"
                    f"<p>{a.get('message')} • Current: <strong>{a.get('current_value')}</strong></p>"
                    f"</div>"
                    f"</div>"
                )
            anomaly_feed_html = "\n".join(items)

        # Delinquency color
        delinquency_pct = validators.get("delinquency_rate_pct", 0.0)
        delinquency_color = "#14F195" if delinquency_pct < 2.5 else ("#F59E0B" if delinquency_pct < 5.0 else "#EF4444")

        # 24h delta classes
        tvl_chg = tvl.get("tvl_change_24h_pct", 0.0)
        tvl_7d_chg = tvl.get("tvl_change_7d_pct", 0.0)
        price_chg = market.get("change_24h_pct", 0.0)

        replacements = {
            "{{ generated_at_utc }}": str(meta.get("generated_at_utc", "N/A")),
            "{{ health_score }}": str(score),
            "{{ health_status }}": str(health.get("status", "OPTIMAL")),
            "{{ health_dashoffset }}": str(dashoffset),
            "{{ pillar_liveness }}": str(pillars.get("liveness", 0)),
            "{{ pillar_liveness_pct }}": str(liveness_pct),
            "{{ pillar_throughput }}": str(pillars.get("throughput", 0)),
            "{{ pillar_throughput_pct }}": str(throughput_pct),
            "{{ pillar_security }}": str(pillars.get("security", 0)),
            "{{ pillar_security_pct }}": str(security_pct),
            "{{ pillar_economic }}": str(pillars.get("economic", 0)),
            "{{ pillar_economic_pct }}": str(economic_pct),
            "{{ current_tps }}": f"{network.get('current_tps', 0.0):,.1f}",
            "{{ avg_tps }}": f"{network.get('avg_tps_1h', 0.0):,.1f}",
            "{{ peak_tps }}": f"{network.get('peak_tps_1h', 0.0):,.1f}",
            "{{ epoch }}": str(network.get("epoch", 0)),
            "{{ epoch_progress_pct }}": str(network.get("epoch_progress_pct", 0.0)),
            "{{ current_slot }}": f"{network.get('current_slot', 0):,}",
            "{{ current_slot_time_ms }}": str(network.get("current_slot_time_ms", 400.0)),
            "{{ current_tvl_b }}": f"{tvl.get('current_tvl_usd', 0.0) / 1e9:.2f}",
            "{{ tvl_change_24h_pct }}": f"{tvl_chg:+.2f}%",
            "{{ tvl_change_7d_pct }}": f"{tvl_7d_chg:+.2f}%",
            "{{ tvl_7d_class }}": "delta-up" if tvl_7d_chg >= 0 else "delta-down",
            "{{ nakamoto_coefficient }}": str(validators.get("nakamoto_coefficient", 19)),
            "{{ active_validators }}": f"{validators.get('active_validators', 0):,}",
            "{{ delinquent_validators }}": str(validators.get("delinquent_validators", 0)),
            "{{ delinquency_rate_pct }}": f"{delinquency_pct:.2f}",
            "{{ delinquency_color }}": delinquency_color,
            "{{ total_active_stake_sol }}": f"{validators.get('total_active_stake_sol', 0.0) / 1e6:.1f}",
            "{{ total_active_stake_sol_raw }}": str(validators.get("total_active_stake_sol", 0.0)),
            "{{ sol_price }}": f"{market.get('price_usd', 0.0):,.2f}",
            "{{ price_change_24h_pct }}": f"{price_chg:+.2f}%",
            "{{ price_change_class }}": "delta-up" if price_chg >= 0 else "delta-down",
            "{{ dex_volume_24h_b }}": f"{dex.get('dex_volume_24h_usd', 0.0) / 1e9:.2f}",
            "{{ dex_volume_7d_b }}": f"{dex.get('dex_volume_7d_usd', 0.0) / 1e9:.2f}",
            "{{ market_cap_b }}": f"{market.get('market_cap_usd_est', 0.0) / 1e9:.2f}",
            "{{ circulating_supply_m }}": f"{supply.get('circulating_supply_sol', 0.0) / 1e6:.1f}",
            "{{ median_tx_fee_usd }}": f"{market.get('median_tx_fee_usd', 0.0):.5f}",
            "{{ median_tx_fee_sol }}": f"{market.get('median_tx_fee_sol', 0.0):.6f}",
            "{{ total_stablecoins_b }}": f"{stables.get('total_stablecoins_usd', 0.0) / 1e9:.2f}",
            "{{ usd_stables_b }}": f"{stables.get('usd_pegged_stables', 0.0) / 1e9:.2f}",
            "{{ eur_stables_m }}": f"{stables.get('eur_pegged_stables', 0.0) / 1e6:.1f}",
            "{{ cad_stables }}": f"{stables.get('cad_pegged_stables', 0.0):,.0f}",
            "{{ protocols_table_rows }}": protocols_table_rows,
            "{{ anomaly_badge_text }}": anomaly_badge_text,
            "{{ anomaly_feed_html }}": anomaly_feed_html,
            "{{ tps_history_json }}": json.dumps(network.get("tps_history", [])),
            "{{ tvl_labels_json }}": json.dumps(tvl_labels),
            "{{ tvl_values_json }}": json.dumps(tvl_values),
            "{{ top_validators_json }}": json.dumps(validators.get("top_10_validators", []))
        }

        rendered = template
        for k, v in replacements.items():
            rendered = rendered.replace(k, v)

        self.output_path.write_text(rendered, encoding="utf-8")
        return str(self.output_path)
