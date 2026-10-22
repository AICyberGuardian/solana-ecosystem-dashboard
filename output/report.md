# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-10-22T05:13:37Z` | **Health Score:** `86.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **86.0/100**.
Current network throughput stands at **1,458.8 TPS** (1-hour average: 1,577.8 TPS) with an average slot generation interval of **212.3 ms**.
Total value locked across Solana DeFi protocols totals **$5.98B** (+0.04% 24h delta), backed by **$15.93B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `459,912,299` | N/A | Active |
| Block Height | `437,946,204` | N/A | Active |
| Current Epoch | `1064` (61.18% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,458.8 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `2,158.6` / `1,215.8 TPS` | N/A | Measured |
| Slot Duration | `212.8 ms` | ~400.0 ms | Normal |
| Total Transactions | `563,164,318,990` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 668 nodes
- **Delinquent Validators:** 9 nodes (1.33% delinquency rate)
- **Total Active Stake:** 438,845,972.81 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `CcaHc2L4...BzoTN1` | 17,130,984.1 SOL | 3.90% | 7% |
| #2 | `he1iusun...PauBtk` | 15,955,653.3 SOL | 3.64% | 0% |
| #3 | `3N7s9zXM...eWiD5g` | 12,545,893.8 SOL | 2.86% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,933,490.6 SOL | 2.49% | 0% |
| #5 | `CatzoSMU...gZDiqb` | 9,728,193.3 SOL | 2.22% | 5% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$105.23` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$62.04B` | 589.6M SOL circulating |
| 24h DEX Trading Volume | `$2.28B` | -6.54% delta |
| Total DeFi TVL | `$5.98B` | +0.04% delta |
| Circulating Stablecoins | `$15.93B` | USD: $15.86B, CAD: $1,443 |
| Median Transaction Fee | `$0.00105` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

✅ **All Systems Nominal.** Zero telemetry anomalies detected across latency, throughput, validator delinquency, TVL, and spot price bounds.

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
