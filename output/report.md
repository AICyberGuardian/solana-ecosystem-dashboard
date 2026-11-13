# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-13T22:29:54Z` | **Health Score:** `77.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **77.0/100**.
Current network throughput stands at **1,736.0 TPS** (1-hour average: 2,557.9 TPS) with an average slot generation interval of **215.4 ms**.
Total value locked across Solana DeFi protocols totals **$4.96B** (-1.53% 24h delta), backed by **$13.93B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `469,093,885` | N/A | Active |
| Block Height | `447,109,039` | N/A | Active |
| Current Epoch | `1085` (86.55% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,736.0 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `3,489.4` / `1,610.3 TPS` | N/A | Measured |
| Slot Duration | `215.1 ms` | ~400.0 ms | Normal |
| Total Transactions | `566,576,293,684` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 660 nodes
- **Delinquent Validators:** 39 nodes (5.58% delinquency rate)
- **Total Active Stake:** 431,736,109.58 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 16,815,754.9 SOL | 3.90% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,140,175.4 SOL | 3.74% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 12,976,229.3 SOL | 3.01% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,117,721.9 SOL | 2.34% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,699,456.4 SOL | 2.25% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$78.52` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$46.45B` | 591.5M SOL circulating |
| 24h DEX Trading Volume | `$1.50B` | -7.06% delta |
| Total DeFi TVL | `$4.96B` | -1.53% delta |
| Circulating Stablecoins | `$13.93B` | USD: $13.84B, CAD: $1,420 |
| Median Transaction Fee | `$0.00079` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Transaction Throughput (TPS)** | `1736.0 TPS` | `~2557.9 TPS` | Current throughput is 32.1% below 1-hour average. |
| `WARNING` | **Validator Delinquency Rate** | `5.58%` | `<= 5.0%` | 5.58% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
