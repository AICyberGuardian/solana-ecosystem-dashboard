# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-15T15:27:22Z` | **Health Score:** `77.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **77.0/100**.
Current network throughput stands at **1,317.1 TPS** (1-hour average: 1,543.2 TPS) with an average slot generation interval of **215.1 ms**.
Total value locked across Solana DeFi protocols totals **$4.74B** (-2.27% 24h delta), backed by **$15.65B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `469,779,494` | N/A | Active |
| Block Height | `447,794,482` | N/A | Active |
| Current Epoch | `1087` (45.25% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,317.1 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `2,138.1` / `1,196.0 TPS` | N/A | Measured |
| Slot Duration | `219.0 ms` | ~400.0 ms | Normal |
| Total Transactions | `566,812,851,137` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 662 nodes
- **Delinquent Validators:** 38 nodes (5.43% delinquency rate)
- **Total Active Stake:** 428,967,833.35 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 16,927,749.2 SOL | 3.95% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,404,543.8 SOL | 3.82% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 12,614,560.7 SOL | 2.94% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,141,932.0 SOL | 2.36% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,754,208.3 SOL | 2.27% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$71.19` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$42.12B` | 591.6M SOL circulating |
| 24h DEX Trading Volume | `$1.69B` | +8.45% delta |
| Total DeFi TVL | `$4.74B` | -2.27% delta |
| Circulating Stablecoins | `$15.65B` | USD: $15.56B, CAD: $1,420 |
| Median Transaction Fee | `$0.00071` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Validator Delinquency Rate** | `5.43%` | `<= 5.0%` | 5.43% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
