import unittest
from unittest.mock import patch, MagicMock
from src.collectors.rpc_collector import SolanaRPCCollector
from src.collectors.defillama_collector import DeFiLlamaCollector
from src.collectors.market_collector import MarketCollector

class TestCollectors(unittest.TestCase):

    def test_rpc_collector_fallback(self):
        collector = SolanaRPCCollector(rpc_urls=["https://invalid-rpc-1.test", "https://invalid-rpc-2.test"])
        with self.assertRaises(ConnectionError):
            collector.call_rpc("getHealth")

    @patch("src.collectors.rpc_collector.SolanaRPCCollector.call_rpc")
    def test_rpc_network_telemetry_parsing(self, mock_rpc):
        def rpc_side_effect(method, params=None):
            if method == "getHealth":
                return "ok"
            elif method == "getEpochInfo":
                return {
                    "epoch": 650,
                    "slotIndex": 216000,
                    "slotsInEpoch": 432000,
                    "absoluteSlot": 280000000,
                    "blockHeight": 260000000,
                    "transactionCount": 500000000000
                }
            elif method == "getRecentPerformanceSamples":
                return [
                    {"numTransactions": 240000, "samplePeriodSecs": 60, "numSlots": 150}
                ]
            return None

        mock_rpc.side_effect = rpc_side_effect
        collector = SolanaRPCCollector()
        res = collector.collect_network_telemetry()

        self.assertEqual(res["health"], "ok")
        self.assertEqual(res["epoch"], 650)
        self.assertEqual(res["epoch_progress_pct"], 50.0)
        self.assertEqual(res["current_tps"], 4000.0)
        self.assertEqual(res["current_slot_time_ms"], 400.0)

    @patch("src.collectors.market_collector.MarketCollector._fetch_binance")
    @patch("src.collectors.market_collector.MarketCollector._fetch_coinbase")
    def test_market_collector_calculation(self, mock_cb, mock_bin):
        mock_bin.return_value = {
            "source": "Binance",
            "price_usd": 150.0,
            "change_24h_pct": 5.0,
            "high_24h_usd": 155.0,
            "low_24h_usd": 142.0,
            "volume_24h_usd": 800000000.0
        }
        collector = MarketCollector()
        res = collector.collect_market_data(circulating_supply_sol=400000000.0)

        self.assertEqual(res["price_usd"], 150.0)
        self.assertEqual(res["market_cap_usd_est"], 60000000000.0)
        self.assertAlmostEqual(res["median_tx_fee_usd"], 0.0015, places=4)

if __name__ == "__main__":
    unittest.main()
