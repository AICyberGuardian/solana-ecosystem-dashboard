# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-13T01:21:44Z` | **Health Score:** `84.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **84.0/100**.
Current network throughput stands at **1,928.2 TPS** (1-hour average: 2,086.0 TPS) with an average slot generation interval of **215.8 ms**.
Total value locked across Solana DeFi protocols totals **$5.04B** (+0.54% 24h delta), backed by **$14.11B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `468,740,768` | N/A | Active |
| Block Height | `446,756,254` | N/A | Active |
| Current Epoch | `1085` (4.81% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,928.2 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `2,710.3` / `1,699.3 TPS` | N/A | Measured |
| Slot Duration | `214.3 ms` | ~400.0 ms | Normal |
| Total Transactions | `566,434,377,428` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 659 nodes
- **Delinquent Validators:** 40 nodes (5.72% delinquency rate)
- **Total Active Stake:** 431,840,381.79 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 16,815,754.9 SOL | 3.89% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,140,175.4 SOL | 3.74% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 12,976,229.3 SOL | 3.00% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,117,721.9 SOL | 2.34% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,699,456.4 SOL | 2.25% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$81.29` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$48.08B` | 591.5M SOL circulating |
| 24h DEX Trading Volume | `$1.61B` | -0.27% delta |
| Total DeFi TVL | `$5.04B` | +0.54% delta |
| Circulating Stablecoins | `$14.11B` | USD: $14.03B, CAD: $1,420 |
| Median Transaction Fee | `$0.00081` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Validator Delinquency Rate** | `5.72%` | `<= 5.0%` | 5.72% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
