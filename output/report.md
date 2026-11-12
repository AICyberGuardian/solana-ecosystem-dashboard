# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-12T03:43:37Z` | **Health Score:** `80.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **80.0/100**.
Current network throughput stands at **1,387.5 TPS** (1-hour average: 1,571.8 TPS) with an average slot generation interval of **215.1 ms**.
Total value locked across Solana DeFi protocols totals **$5.06B** (+0.53% 24h delta), backed by **$13.95B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `468,378,727` | N/A | Active |
| Block Height | `446,394,651` | N/A | Active |
| Current Epoch | `1084` (21.0% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,387.5 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `2,107.8` / `1,233.0 TPS` | N/A | Measured |
| Slot Duration | `218.2 ms` | ~400.0 ms | Normal |
| Total Transactions | `566,296,561,368` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 661 nodes
- **Delinquent Validators:** 37 nodes (5.30% delinquency rate)
- **Total Active Stake:** 432,731,490.40 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 16,789,054.4 SOL | 3.88% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,119,193.9 SOL | 3.73% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 13,026,247.1 SOL | 3.01% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,116,092.2 SOL | 2.34% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,681,376.1 SOL | 2.24% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$83.12` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$49.16B` | 591.5M SOL circulating |
| 24h DEX Trading Volume | `$1.64B` | +22.25% delta |
| Total DeFi TVL | `$5.06B` | +0.53% delta |
| Circulating Stablecoins | `$13.95B` | USD: $13.87B, CAD: $1,421 |
| Median Transaction Fee | `$0.00083` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Validator Delinquency Rate** | `5.30%` | `<= 5.0%` | 5.30% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
