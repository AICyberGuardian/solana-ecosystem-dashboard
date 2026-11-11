# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-11T16:28:27Z` | **Health Score:** `80.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **80.0/100**.
Current network throughput stands at **1,721.1 TPS** (1-hour average: 2,370.0 TPS) with an average slot generation interval of **214.7 ms**.
Total value locked across Solana DeFi protocols totals **$5.08B** (+0.57% 24h delta), backed by **$14.47B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `468,190,370` | N/A | Active |
| Block Height | `446,206,637` | N/A | Active |
| Current Epoch | `1083` (77.4% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,721.1 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `3,321.2` / `1,721.1 TPS` | N/A | Measured |
| Slot Duration | `216.6 ms` | ~400.0 ms | Normal |
| Total Transactions | `566,207,716,156` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 659 nodes
- **Delinquent Validators:** 40 nodes (5.72% delinquency rate)
- **Total Active Stake:** 432,468,095.94 SOL
- **Nakamoto Coefficient:** `16` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 16,764,484.7 SOL | 3.88% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,564,684.9 SOL | 3.83% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 13,031,624.9 SOL | 3.01% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,117,254.3 SOL | 2.34% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,644,050.7 SOL | 2.23% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$84.82` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$50.16B` | 591.4M SOL circulating |
| 24h DEX Trading Volume | `$1.34B` | -9.79% delta |
| Total DeFi TVL | `$5.08B` | +0.57% delta |
| Circulating Stablecoins | `$14.47B` | USD: $14.39B, CAD: $1,423 |
| Median Transaction Fee | `$0.00085` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Transaction Throughput (TPS)** | `1721.1 TPS` | `~2370.0 TPS` | Current throughput is 27.4% below 1-hour average. |
| `WARNING` | **Validator Delinquency Rate** | `5.72%` | `<= 5.0%` | 5.72% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
