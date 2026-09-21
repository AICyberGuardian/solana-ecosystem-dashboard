import unittest
from src.analysis.anomaly_detector import AnomalyDetector
from src.analysis.health_score import HealthScoreEngine

class TestAnalysis(unittest.TestCase):

    def setUp(self):
        self.detector = AnomalyDetector()
        self.health_engine = HealthScoreEngine()

    def test_anomaly_detector_nominal(self):
        telemetry = {
            "network": {
                "health": "ok",
                "current_tps": 4000.0,
                "avg_tps_1h": 4100.0,
                "current_slot_time_ms": 410.0
            },
            "validators": {
                "delinquency_rate_pct": 1.2,
                "nakamoto_coefficient": 19
            },
            "defi": {
                "tvl": {"tvl_change_24h_pct": 2.0}
            },
            "market": {
                "change_24h_pct": 3.0
            }
        }
        anomalies = self.detector.analyze(telemetry)
        self.assertEqual(len(anomalies), 0)

    def test_anomaly_detector_tps_drop(self):
        telemetry = {
            "network": {
                "health": "ok",
                "current_tps": 2000.0,
                "avg_tps_1h": 4000.0,  # 50% drop
                "current_slot_time_ms": 400.0
            },
            "validators": {"delinquency_rate_pct": 1.0, "nakamoto_coefficient": 19},
            "defi": {"tvl": {"tvl_change_24h_pct": 1.0}},
            "market": {"change_24h_pct": 1.0}
        }
        anomalies = self.detector.analyze(telemetry)
        self.assertTrue(any(a["metric"] == "Transaction Throughput (TPS)" for a in anomalies))

    def test_health_score_optimal(self):
        telemetry = {
            "network": {"health": "ok", "current_tps": 4500.0, "avg_tps_1h": 4400.0, "current_slot_time_ms": 410.0},
            "validators": {"delinquency_rate_pct": 0.8, "nakamoto_coefficient": 19},
            "defi": {
                "tvl": {"current_tvl_usd": 6500000000.0},
                "dex": {"dex_volume_24h_usd": 2000000000.0},
                "stablecoins": {"total_stablecoins_usd": 15000000000.0}
            }
        }
        res = self.health_engine.compute(telemetry)
        self.assertEqual(res["status"], "OPTIMAL")
        self.assertGreaterEqual(res["score"], 90.0)

if __name__ == "__main__":
    unittest.main()
