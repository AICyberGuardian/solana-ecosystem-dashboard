# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-19T08:39:59Z` | **Health Score:** `80.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **80.0/100**.
Current network throughput stands at **1,232.2 TPS** (1-hour average: 1,232.0 TPS) with an average slot generation interval of **215.4 ms**.
Total value locked across Solana DeFi protocols totals **$4.79B** (-0.10% 24h delta), backed by **$12.67B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `471,272,089` | N/A | Active |
| Block Height | `449,286,392` | N/A | Active |
| Current Epoch | `1090` (90.76% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,232.2 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `1,526.5` / `979.4 TPS` | N/A | Measured |
| Slot Duration | `215.1 ms` | ~400.0 ms | Normal |
| Total Transactions | `567,392,530,162` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 660 nodes
- **Delinquent Validators:** 25 nodes (3.65% delinquency rate)
- **Total Active Stake:** 426,680,594.93 SOL
- **Nakamoto Coefficient:** `16` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 17,030,758.6 SOL | 3.99% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,476,078.1 SOL | 3.86% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 12,423,469.9 SOL | 2.91% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,297,722.4 SOL | 2.41% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,815,429.7 SOL | 2.30% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$74.36` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$44.01B` | 591.8M SOL circulating |
| 24h DEX Trading Volume | `$1.70B` | +12.72% delta |
| Total DeFi TVL | `$4.79B` | -0.10% delta |
| Circulating Stablecoins | `$12.67B` | USD: $12.59B, CAD: $1,414 |
| Median Transaction Fee | `$0.00074` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

✅ **All Systems Nominal.** Zero telemetry anomalies detected across latency, throughput, validator delinquency, TVL, and spot price bounds.

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
