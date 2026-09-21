import unittest
import tempfile
import os
import json
from pathlib import Path
from src.generators.json_generator import JSONGenerator
from src.generators.markdown_generator import MarkdownGenerator
from src.generators.html_generator import HTMLGenerator

class TestGenerators(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.data = {
            "meta": {"generated_at_utc": "2026-09-21T12:00:00Z"},
            "network": {
                "health": "ok",
                "current_tps": 4200.0,
                "avg_tps_1h": 4100.0,
                "peak_tps_1h": 5000.0,
                "epoch": 650,
                "epoch_progress_pct": 75.0,
                "current_slot": 290000000,
                "current_slot_time_ms": 405.0,
                "tps_history": [4000, 4100, 4200]
            },
            "validators": {
                "active_validators": 675,
                "delinquent_validators": 5,
                "delinquency_rate_pct": 0.74,
                "total_active_stake_sol": 390000000.0,
                "nakamoto_coefficient": 18,
                "top_10_validators": []
            },
            "supply": {"circulating_supply_sol": 468000000.0},
            "defi": {
                "tvl": {"current_tvl_usd": 6200000000.0, "tvl_change_24h_pct": 1.5, "tvl_change_7d_pct": 3.0, "history_30d": []},
                "dex": {"dex_volume_24h_usd": 2100000000.0, "dex_volume_7d_usd": 14000000000.0, "dex_volume_change_24h_pct": 2.1},
                "stablecoins": {"total_stablecoins_usd": 15500000000.0, "usd_pegged_stables": 15400000000.0, "eur_pegged_stables": 60000000.0, "cad_pegged_stables": 1500.0},
                "top_protocols": []
            },
            "market": {
                "price_usd": 120.0,
                "change_24h_pct": 4.5,
                "market_cap_usd_est": 56000000000.0,
                "median_tx_fee_usd": 0.0012,
                "median_tx_fee_sol": 0.00001,
                "source": "Binance"
            },
            "health_score": {
                "score": 93.0,
                "status": "OPTIMAL",
                "pillars": {"liveness": 25.0, "throughput": 25.0, "security": 18.0, "economic": 25.0}
            },
            "anomalies": []
        }

    def tearDown(self):
        self.test_dir.cleanup()

    def test_json_generator(self):
        out_path = os.path.join(self.test_dir.name, "data.json")
        gen = JSONGenerator(out_path)
        gen.generate(self.data)
        self.assertTrue(os.path.exists(out_path))
        with open(out_path, encoding="utf-8") as f:
            loaded = json.load(f)
        self.assertEqual(loaded["health_score"]["score"], 93.0)

    def test_markdown_generator(self):
        out_path = os.path.join(self.test_dir.name, "report.md")
        gen = MarkdownGenerator(out_path)
        gen.generate(self.data)
        self.assertTrue(os.path.exists(out_path))
        content = Path(out_path).read_text(encoding="utf-8")
        self.assertIn("OPTIMAL", content)
        self.assertIn("Nakamoto Coefficient", content)

    def test_html_generator(self):
        out_path = os.path.join(self.test_dir.name, "dashboard.html")
        template_path = os.path.join(os.path.dirname(__file__), "..", "templates", "dashboard.html")
        gen = HTMLGenerator(template_path=template_path, output_path=out_path)
        gen.generate(self.data)
        self.assertTrue(os.path.exists(out_path))
        content = Path(out_path).read_text(encoding="utf-8")
        self.assertIn("SOLANA ECOSYSTEM INTELLIGENCE", content)
        self.assertNotIn("{{ health_score }}", content)

if __name__ == "__main__":
    unittest.main()
