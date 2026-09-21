import urllib.request
import urllib.error
import json
import time
from typing import Dict, Any, Optional

class MarketCollector:
    """Collects spot SOL price, 24h metrics, and economic indicators with multi-exchange failover and zero API keys."""

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def _fetch_binance(self) -> Optional[Dict[str, Any]]:
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=SOLUSDT"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "SolanaEcosystemDashboard/1.0", "Accept": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode("utf-8"))
                    price = float(data.get("lastPrice", 0.0))
                    change_pct = float(data.get("priceChangePercent", 0.0))
                    high_24h = float(data.get("highPrice", 0.0))
                    low_24h = float(data.get("lowPrice", 0.0))
                    volume_usd = float(data.get("quoteVolume", 0.0))
                    return {
                        "source": "Binance",
                        "price_usd": round(price, 2),
                        "change_24h_pct": round(change_pct, 2),
                        "high_24h_usd": round(high_24h, 2),
                        "low_24h_usd": round(low_24h, 2),
                        "volume_24h_usd": round(volume_usd, 2)
                    }
        except Exception:
            return None
        return None

    def _fetch_coinbase(self) -> Optional[Dict[str, Any]]:
        url = "https://api.coinbase.com/v2/prices/SOL-USD/spot"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "SolanaEcosystemDashboard/1.0", "Accept": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode("utf-8"))
                    price = float(data.get("data", {}).get("amount", 0.0))
                    return {
                        "source": "Coinbase",
                        "price_usd": round(price, 2),
                        "change_24h_pct": 0.0,
                        "high_24h_usd": round(price, 2),
                        "low_24h_usd": round(price, 2),
                        "volume_24h_usd": 0.0
                    }
        except Exception:
            return None
        return None

    def collect_market_data(self, circulating_supply_sol: float = 468000000.0) -> Dict[str, Any]:
        """Collects price, 24h change, market cap, and economic indicators."""
        metrics = self._fetch_binance() or self._fetch_coinbase()
        if not metrics:
            # Safe fallback if network is completely unreachable
            metrics = {
                "source": "Fallback-Estimator",
                "price_usd": 118.50,
                "change_24h_pct": 0.0,
                "high_24h_usd": 120.0,
                "low_24h_usd": 115.0,
                "volume_24h_usd": 500000000.0
            }

        price = metrics["price_usd"]
        market_cap_est = round(price * circulating_supply_sol, 2)
        metrics["market_cap_usd_est"] = market_cap_est
        
        # Real Economic Value (REV) calculation / base transaction fee estimate
        # Baseline Solana median tx fee: ~0.000005 to 0.000015 SOL (~$0.0006 - $0.0018)
        metrics["median_tx_fee_sol"] = 0.000010
        metrics["median_tx_fee_usd"] = round(price * 0.000010, 5)

        return metrics
