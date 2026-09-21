import urllib.request
import urllib.error
import json
import time
from typing import Dict, Any, List, Optional

class DeFiLlamaCollector:
    """Collects DeFi, TVL, DEX volume, and Stablecoin metrics from DeFiLlama public endpoints with zero API keys."""

    BASE_URL = "https://api.llama.fi"
    STABLECOINS_URL = "https://stablecoins.llama.fi"

    def __init__(self, timeout: int = 15):
        self.timeout = timeout

    def _get_json(self, url: str) -> Optional[Any]:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "SolanaEcosystemDashboard/1.0 (SuperteamCanada; open-source)",
                "Accept": "application/json"
            }
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                if resp.status == 200:
                    return json.loads(resp.read().decode("utf-8"))
        except Exception:
            return None
        return None

    def collect_chain_tvl(self) -> Dict[str, Any]:
        """Fetches current Solana TVL and 24h / 7d historical delta."""
        chains = self._get_json(f"{self.BASE_URL}/v2/chains") or []
        sol_chain = next((c for c in chains if c.get("name") == "Solana"), {})
        current_tvl = sol_chain.get("tvl", 0.0)

        # Historical TVL curve (last 30 days)
        history = self._get_json(f"{self.BASE_URL}/v2/historicalChainTvl/Solana") or []
        recent_30d = history[-30:] if len(history) >= 30 else history
        
        tvl_change_24h_pct = 0.0
        tvl_change_7d_pct = 0.0
        if len(recent_30d) >= 2:
            prev_day = recent_30d[-2].get("tvl", 0)
            if prev_day > 0:
                tvl_change_24h_pct = round(((current_tvl - prev_day) / prev_day) * 100, 2)
        if len(recent_30d) >= 8:
            week_ago = recent_30d[-8].get("tvl", 0)
            if week_ago > 0:
                tvl_change_7d_pct = round(((current_tvl - week_ago) / week_ago) * 100, 2)

        chart_data = []
        for pt in recent_30d:
            chart_data.append({
                "date": time.strftime("%b %d", time.gmtime(pt.get("date", 0))),
                "tvl_usd": round(pt.get("tvl", 0), 2)
            })

        return {
            "current_tvl_usd": round(current_tvl, 2),
            "tvl_change_24h_pct": tvl_change_24h_pct,
            "tvl_change_7d_pct": tvl_change_7d_pct,
            "history_30d": chart_data
        }

    def collect_dex_volume(self) -> Dict[str, Any]:
        """Fetches 24h & 7d DEX trading volumes on Solana."""
        dex_data = self._get_json(f"{self.BASE_URL}/overview/dexs/solana") or {}
        total_24h = dex_data.get("total24h", 0.0) or 0.0
        total_7d = dex_data.get("total7d", 0.0) or 0.0
        change_1d = dex_data.get("change_1d", 0.0) or 0.0

        return {
            "dex_volume_24h_usd": round(float(total_24h), 2),
            "dex_volume_7d_usd": round(float(total_7d), 2),
            "dex_volume_change_24h_pct": round(float(change_1d), 2)
        }

    def collect_stablecoins(self) -> Dict[str, Any]:
        """Fetches total stablecoin market cap circulating on Solana."""
        chains = self._get_json(f"{self.STABLECOINS_URL}/stablecoinchains") or []
        sol_stables = next((c for c in chains if c.get("name") == "Solana"), {})
        circulating = sol_stables.get("totalCirculatingUSD", {})

        usd_stables = circulating.get("peggedUSD", 0.0)
        eur_stables = circulating.get("peggedEUR", 0.0)
        cad_stables = circulating.get("peggedCAD", 0.0)
        total_stables = sum(circulating.values()) if circulating else 0.0

        return {
            "total_stablecoins_usd": round(total_stables, 2),
            "usd_pegged_stables": round(usd_stables, 2),
            "eur_pegged_stables": round(eur_stables, 2),
            "cad_pegged_stables": round(cad_stables, 2)
        }

    def collect_top_protocols(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Fetches top protocols deployed on Solana sorted by TVL."""
        protocols = self._get_json(f"{self.BASE_URL}/protocols") or []
        sol_protocols = []
        for p in protocols:
            if "Solana" in p.get("chains", []):
                chain_tvl = p.get("chainTvls", {}).get("Solana", 0.0)
                if chain_tvl > 0:
                    sol_protocols.append({
                        "name": p.get("name"),
                        "category": p.get("category", "General"),
                        "tvl_usd": round(chain_tvl, 2),
                        "change_1d": round(p.get("change_1d", 0.0) or 0.0, 2),
                        "change_7d": round(p.get("change_7d", 0.0) or 0.0, 2),
                        "url": p.get("url", "")
                    })

        sol_protocols.sort(key=lambda x: x["tvl_usd"], reverse=True)
        return sol_protocols[:limit]

    def collect_all(self) -> Dict[str, Any]:
        """Runs all DeFiLlama metrics collection."""
        return {
            "tvl": self.collect_chain_tvl(),
            "dex": self.collect_dex_volume(),
            "stablecoins": self.collect_stablecoins(),
            "top_protocols": self.collect_top_protocols(8)
        }
