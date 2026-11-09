# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-09T05:10:25Z` | **Health Score:** `78.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **78.0/100**.
Current network throughput stands at **1,071.8 TPS** (1-hour average: 1,232.3 TPS) with an average slot generation interval of **214.9 ms**.
Total value locked across Solana DeFi protocols totals **$5.14B** (-0.85% 24h delta), backed by **$14.82B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `467,195,060` | N/A | Active |
| Block Height | `445,213,117` | N/A | Active |
| Current Epoch | `1081` (47.0% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,071.8 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `1,838.4` / `917.3 TPS` | N/A | Measured |
| Slot Duration | `207.6 ms` | ~400.0 ms | Normal |
| Total Transactions | `565,860,400,208` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 662 nodes
- **Delinquent Validators:** 35 nodes (5.02% delinquency rate)
- **Total Active Stake:** 433,293,949.85 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `CcaHc2L4...BzoTN1` | 17,050,552.6 SOL | 3.94% | 7% |
| #2 | `he1iusun...PauBtk` | 16,720,131.0 SOL | 3.86% | 0% |
| #3 | `3N7s9zXM...eWiD5g` | 13,021,912.5 SOL | 3.00% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,279,070.0 SOL | 2.37% | 0% |
| #5 | `CatzoSMU...gZDiqb` | 9,553,388.1 SOL | 2.21% | 5% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$87.07` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$51.47B` | 591.1M SOL circulating |
| 24h DEX Trading Volume | `$1.00B` | +8.68% delta |
| Total DeFi TVL | `$5.14B` | -0.85% delta |
| Circulating Stablecoins | `$14.82B` | USD: $14.74B, CAD: $1,436 |
| Median Transaction Fee | `$0.00087` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Validator Delinquency Rate** | `5.02%` | `<= 5.0%` | 5.02% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
