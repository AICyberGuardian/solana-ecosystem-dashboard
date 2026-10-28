# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-10-28T00:18:04Z` | **Health Score:** `84.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **84.0/100**.
Current network throughput stands at **1,803.9 TPS** (1-hour average: 1,832.4 TPS) with an average slot generation interval of **213.2 ms**.
Total value locked across Solana DeFi protocols totals **$5.74B** (+0.59% 24h delta), backed by **$15.50B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `462,270,506` | N/A | Active |
| Block Height | `440,295,257` | N/A | Active |
| Current Epoch | `1070` (7.06% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,803.9 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `2,416.5` / `1,240.2 TPS` | N/A | Measured |
| Slot Duration | `215.1 ms` | ~400.0 ms | Normal |
| Total Transactions | `564,071,549,572` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 662 nodes
- **Delinquent Validators:** 29 nodes (4.20% delinquency rate)
- **Total Active Stake:** 433,415,732.94 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `CcaHc2L4...BzoTN1` | 17,006,421.9 SOL | 3.92% | 7% |
| #2 | `he1iusun...PauBtk` | 16,661,096.4 SOL | 3.84% | 0% |
| #3 | `3N7s9zXM...eWiD5g` | 12,791,931.1 SOL | 2.95% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,815,143.1 SOL | 2.50% | 0% |
| #5 | `CatzoSMU...gZDiqb` | 9,718,548.1 SOL | 2.24% | 5% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$101.10` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$59.64B` | 589.9M SOL circulating |
| 24h DEX Trading Volume | `$2.07B` | +42.91% delta |
| Total DeFi TVL | `$5.74B` | +0.59% delta |
| Circulating Stablecoins | `$15.50B` | USD: $15.43B, CAD: $1,444 |
| Median Transaction Fee | `$0.00101` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

✅ **All Systems Nominal.** Zero telemetry anomalies detected across latency, throughput, validator delinquency, TVL, and spot price bounds.

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
