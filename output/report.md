# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-14T09:53:24Z` | **Health Score:** `77.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **77.0/100**.
Current network throughput stands at **994.0 TPS** (1-hour average: 1,103.0 TPS) with an average slot generation interval of **215.1 ms**.
Total value locked across Solana DeFi protocols totals **$4.84B** (-3.25% 24h delta), backed by **$13.94B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `469,284,551` | N/A | Active |
| Block Height | `447,299,650` | N/A | Active |
| Current Epoch | `1086` (30.68% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `994.0 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `1,547.0` / `893.0 TPS` | N/A | Measured |
| Slot Duration | `219.0 ms` | ~400.0 ms | Normal |
| Total Transactions | `566,639,247,992` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 662 nodes
- **Delinquent Validators:** 37 nodes (5.29% delinquency rate)
- **Total Active Stake:** 429,177,602.72 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 16,955,905.0 SOL | 3.95% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,374,908.9 SOL | 3.81% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 12,611,498.3 SOL | 2.94% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,140,468.5 SOL | 2.36% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,736,889.6 SOL | 2.27% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$75.86` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$44.88B` | 591.6M SOL circulating |
| 24h DEX Trading Volume | `$1.45B` | -3.34% delta |
| Total DeFi TVL | `$4.84B` | -3.25% delta |
| Circulating Stablecoins | `$13.94B` | USD: $13.85B, CAD: $1,420 |
| Median Transaction Fee | `$0.00076` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Validator Delinquency Rate** | `5.29%` | `<= 5.0%` | 5.29% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
