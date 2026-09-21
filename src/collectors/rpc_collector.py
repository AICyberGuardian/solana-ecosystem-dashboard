import urllib.request
import urllib.error
import json
import time
from typing import Dict, Any, List, Optional

PUBLIC_RPCS = [
    "https://api.mainnet-beta.solana.com",
    "https://solana-rpc.publicnode.com",
    "https://rpc.ankr.com/solana"
]

class SolanaRPCCollector:
    """Collects direct on-chain telemetry from Solana mainnet RPCs with zero API keys."""

    def __init__(self, rpc_urls: Optional[List[str]] = None, timeout: int = 15):
        self.rpc_urls = rpc_urls or PUBLIC_RPCS
        self.timeout = timeout

    def call_rpc(self, method: str, params: Optional[List[Any]] = None) -> Any:
        """Calls a Solana JSON-RPC 2.0 method with automatic endpoint failover."""
        params = params or []
        payload = json.dumps({
            "jsonrpc": "2.0",
            "id": int(time.time() * 1000),
            "method": method,
            "params": params
        }).encode("utf-8")

        last_error = None
        for rpc in self.rpc_urls:
            try:
                req = urllib.request.Request(
                    rpc,
                    data=payload,
                    headers={
                        "Content-Type": "application/json",
                        "User-Agent": "SolanaEcosystemDashboard/1.0"
                    }
                )
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    res_data = json.loads(resp.read().decode("utf-8"))
                    if "error" in res_data:
                        last_error = res_data["error"]
                        continue
                    return res_data.get("result")
            except Exception as e:
                last_error = e
                continue

        raise ConnectionError(f"All RPC endpoints failed for {method}. Last error: {last_error}")

    def collect_network_telemetry(self) -> Dict[str, Any]:
        """Gathers epoch info, performance samples, TPS, and slot duration."""
        # 1. Health
        health = "unknown"
        try:
            health = self.call_rpc("getHealth")
        except Exception:
            health = "degraded"

        # 2. Epoch Info
        epoch_info = self.call_rpc("getEpochInfo") or {}
        epoch = epoch_info.get("epoch", 0)
        slot_index = epoch_info.get("slotIndex", 0)
        slots_in_epoch = epoch_info.get("slotsInEpoch", 432000)
        epoch_progress_pct = round((slot_index / slots_in_epoch) * 100, 2) if slots_in_epoch > 0 else 0.0
        current_slot = epoch_info.get("absoluteSlot", 0)
        block_height = epoch_info.get("blockHeight", 0)
        tx_count = epoch_info.get("transactionCount", 0)

        # 3. Performance Samples (calculate true TPS and slot time over last 60 samples)
        perf_samples = self.call_rpc("getRecentPerformanceSamples", [60]) or []
        tps_samples = []
        slot_time_samples = []

        for sample in perf_samples:
            num_tx = sample.get("numTransactions", 0)
            sample_sec = sample.get("samplePeriodSecs", 60)
            num_slots = sample.get("numSlots", 0)

            if sample_sec > 0:
                tps_samples.append(round(num_tx / sample_sec, 1))
            if num_slots > 0 and sample_sec > 0:
                # slot time in milliseconds
                slot_time_samples.append(round((sample_sec / num_slots) * 1000, 1))

        current_tps = tps_samples[0] if tps_samples else 0.0
        avg_tps = round(sum(tps_samples) / len(tps_samples), 1) if tps_samples else 0.0
        peak_tps = max(tps_samples) if tps_samples else 0.0
        min_tps = min(tps_samples) if tps_samples else 0.0

        current_slot_time_ms = slot_time_samples[0] if slot_time_samples else 400.0
        avg_slot_time_ms = round(sum(slot_time_samples) / len(slot_time_samples), 1) if slot_time_samples else 400.0

        return {
            "health": health,
            "current_slot": current_slot,
            "block_height": block_height,
            "total_transaction_count": tx_count,
            "epoch": epoch,
            "epoch_slot_index": slot_index,
            "slots_in_epoch": slots_in_epoch,
            "epoch_progress_pct": epoch_progress_pct,
            "current_tps": current_tps,
            "avg_tps_1h": avg_tps,
            "peak_tps_1h": peak_tps,
            "min_tps_1h": min_tps,
            "current_slot_time_ms": current_slot_time_ms,
            "avg_slot_time_ms": avg_slot_time_ms,
            "simd_0525": {
                "target_ms": 350.0,
                "measured_ms": avg_slot_time_ms,
                "delta_ms": round(avg_slot_time_ms - 350.0, 1),
                "status": "OPTIMAL" if avg_slot_time_ms <= 360.0 else "ELEVATED",
                "label": "SIMD-0525 (350ms Target)"
            },
            "tps_history": tps_samples[:30],
            "slot_time_history": slot_time_samples[:30]
        }

    def collect_validator_telemetry(self) -> Dict[str, Any]:
        """Gathers active vs delinquent validators, total active stake, and top nodes."""
        vote_accounts = self.call_rpc("getVoteAccounts") or {}
        current_validators = vote_accounts.get("current", [])
        delinquent_validators = vote_accounts.get("delinquent", [])

        active_count = len(current_validators)
        delinquent_count = len(delinquent_validators)
        total_validators = active_count + delinquent_count
        delinquency_rate_pct = round((delinquent_count / total_validators) * 100, 2) if total_validators > 0 else 0.0

        # Calculate stake in SOL (lamports / 10^9)
        total_active_stake_lamports = sum(v.get("activatedStake", 0) for v in current_validators)
        total_active_stake_sol = round(total_active_stake_lamports / 1e9, 2)

        # Sort top validators by stake
        sorted_validators = sorted(current_validators, key=lambda v: v.get("activatedStake", 0), reverse=True)
        top_10 = []
        cumulative_stake = 0
        nakamoto_threshold = total_active_stake_lamports * 0.3333
        nakamoto_coefficient = 0

        for idx, v in enumerate(sorted_validators):
            stake_lamports = v.get("activatedStake", 0)
            stake_sol = round(stake_lamports / 1e9, 2)
            stake_share_pct = round((stake_lamports / total_active_stake_lamports) * 100, 3) if total_active_stake_lamports > 0 else 0.0

            cumulative_stake += stake_lamports
            if cumulative_stake <= nakamoto_threshold or nakamoto_coefficient == 0:
                nakamoto_coefficient += 1

            if idx < 10:
                top_10.append({
                    "rank": idx + 1,
                    "vote_pubkey": v.get("votePubkey"),
                    "node_pubkey": v.get("nodePubkey"),
                    "stake_sol": stake_sol,
                    "stake_share_pct": stake_share_pct,
                    "commission": v.get("commission", 0),
                    "last_vote": v.get("lastVote", 0)
                })

        return {
            "total_validators": total_validators,
            "active_validators": active_count,
            "delinquent_validators": delinquent_count,
            "delinquency_rate_pct": delinquency_rate_pct,
            "total_active_stake_sol": total_active_stake_sol,
            "nakamoto_coefficient": nakamoto_coefficient,
            "top_10_validators": top_10
        }

    def collect_supply_telemetry(self) -> Dict[str, Any]:
        """Gathers total, circulating, and non-circulating SOL supply."""
        supply_data = self.call_rpc("getSupply") or {}
        val = supply_data.get("value", {})
        total = round(val.get("total", 0) / 1e9, 2)
        circulating = round(val.get("circulating", 0) / 1e9, 2)
        non_circulating = round(val.get("nonCirculating", 0) / 1e9, 2)
        circulating_pct = round((circulating / total) * 100, 2) if total > 0 else 0.0

        return {
            "total_supply_sol": total,
            "circulating_supply_sol": circulating,
            "non_circulating_supply_sol": non_circulating,
            "circulating_supply_pct": circulating_pct
        }

    def collect_all(self) -> Dict[str, Any]:
        """Collects full suite of on-chain data."""
        network = self.collect_network_telemetry()
        validators = self.collect_validator_telemetry()
        supply = self.collect_supply_telemetry()

        return {
            "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "network": network,
            "validators": validators,
            "supply": supply
        }
