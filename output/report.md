# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-11T08:06:35Z` | **Health Score:** `80.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **80.0/100**.
Current network throughput stands at **1,021.3 TPS** (1-hour average: 1,263.7 TPS) with an average slot generation interval of **214.5 ms**.
Total value locked across Solana DeFi protocols totals **$5.05B** (-0.11% 24h delta), backed by **$14.45B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `468,050,165` | N/A | Active |
| Block Height | `446,066,624` | N/A | Active |
| Current Epoch | `1083` (44.95% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,021.3 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `1,690.3` / `1,021.3 TPS` | N/A | Measured |
| Slot Duration | `211.3 ms` | ~400.0 ms | Normal |
| Total Transactions | `566,159,388,166` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 658 nodes
- **Delinquent Validators:** 41 nodes (5.87% delinquency rate)
- **Total Active Stake:** 432,427,661.35 SOL
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
| SOL Spot Price | `$83.14` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$49.17B` | 591.4M SOL circulating |
| 24h DEX Trading Volume | `$1.34B` | -10.18% delta |
| Total DeFi TVL | `$5.05B` | -0.11% delta |
| Circulating Stablecoins | `$14.45B` | USD: $14.36B, CAD: $1,426 |
| Median Transaction Fee | `$0.00083` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Validator Delinquency Rate** | `5.87%` | `<= 5.0%` | 5.87% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
