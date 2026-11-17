# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-17T01:57:37Z` | **Health Score:** `81.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **81.0/100**.
Current network throughput stands at **1,868.5 TPS** (1-hour average: 1,970.5 TPS) with an average slot generation interval of **214.4 ms**.
Total value locked across Solana DeFi protocols totals **$4.75B** (+1.16% 24h delta), backed by **$14.07B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `470,357,584` | N/A | Active |
| Block Height | `448,372,433` | N/A | Active |
| Current Epoch | `1088` (79.07% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,868.5 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `2,577.8` / `1,209.5 TPS` | N/A | Measured |
| Slot Duration | `215.1 ms` | ~400.0 ms | Normal |
| Total Transactions | `567,040,390,717` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 662 nodes
- **Delinquent Validators:** 37 nodes (5.29% delinquency rate)
- **Total Active Stake:** 428,992,845.45 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 16,936,855.4 SOL | 3.95% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,432,361.2 SOL | 3.83% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 12,486,687.0 SOL | 2.91% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,142,841.8 SOL | 2.36% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,787,747.5 SOL | 2.28% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$71.74` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$42.45B` | 591.7M SOL circulating |
| 24h DEX Trading Volume | `$1.40B` | +3.36% delta |
| Total DeFi TVL | `$4.75B` | +1.16% delta |
| Circulating Stablecoins | `$14.07B` | USD: $13.99B, CAD: $1,416 |
| Median Transaction Fee | `$0.00072` | ~0.000010 SOL |

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
