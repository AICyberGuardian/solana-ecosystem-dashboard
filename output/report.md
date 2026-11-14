# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-14T02:39:24Z` | **Health Score:** `81.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **81.0/100**.
Current network throughput stands at **2,121.4 TPS** (1-hour average: 1,817.3 TPS) with an average slot generation interval of **214.9 ms**.
Total value locked across Solana DeFi protocols totals **$4.90B** (-0.38% 24h delta), backed by **$13.96B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `469,163,493` | N/A | Active |
| Block Height | `447,178,632` | N/A | Active |
| Current Epoch | `1086` (2.66% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `2,121.4 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `3,454.9` / `1,073.1 TPS` | N/A | Measured |
| Slot Duration | `217.4 ms` | ~400.0 ms | Normal |
| Total Transactions | `566,602,696,190` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 663 nodes
- **Delinquent Validators:** 36 nodes (5.15% delinquency rate)
- **Total Active Stake:** 429,256,290.88 SOL
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
| SOL Spot Price | `$75.50` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$44.66B` | 591.6M SOL circulating |
| 24h DEX Trading Volume | `$1.45B` | -3.34% delta |
| Total DeFi TVL | `$4.90B` | -0.38% delta |
| Circulating Stablecoins | `$13.96B` | USD: $13.88B, CAD: $1,420 |
| Median Transaction Fee | `$0.00076` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Validator Delinquency Rate** | `5.15%` | `<= 5.0%` | 5.15% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
