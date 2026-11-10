# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-10T21:23:03Z` | **Health Score:** `80.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **80.0/100**.
Current network throughput stands at **1,658.0 TPS** (1-hour average: 1,923.7 TPS) with an average slot generation interval of **213.5 ms**.
Total value locked across Solana DeFi protocols totals **$5.01B** (-1.75% 24h delta), backed by **$14.54B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `467,870,234` | N/A | Active |
| Block Height | `445,887,041` | N/A | Active |
| Current Epoch | `1083` (3.29% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,658.0 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `2,875.0` / `1,271.5 TPS` | N/A | Measured |
| Slot Duration | `212.8 ms` | ~400.0 ms | Normal |
| Total Transactions | `566,093,396,836` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 657 nodes
- **Delinquent Validators:** 42 nodes (6.01% delinquency rate)
- **Total Active Stake:** 427,433,076.32 SOL
- **Nakamoto Coefficient:** `16` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 16,764,484.7 SOL | 3.92% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,564,684.9 SOL | 3.88% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 13,031,624.9 SOL | 3.05% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,117,254.3 SOL | 2.37% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,644,050.7 SOL | 2.26% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$83.28` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$49.24B` | 591.2M SOL circulating |
| 24h DEX Trading Volume | `$1.49B` | +42.59% delta |
| Total DeFi TVL | `$5.01B` | -1.75% delta |
| Circulating Stablecoins | `$14.54B` | USD: $14.46B, CAD: $1,428 |
| Median Transaction Fee | `$0.00083` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Validator Delinquency Rate** | `6.01%` | `<= 5.0%` | 6.01% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
