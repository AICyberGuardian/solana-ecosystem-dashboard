# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-10-25T05:06:37Z` | **Health Score:** `87.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **87.0/100**.
Current network throughput stands at **1,547.3 TPS** (1-hour average: 1,459.5 TPS) with an average slot generation interval of **212.8 ms**.
Total value locked across Solana DeFi protocols totals **$5.80B** (+0.46% 24h delta), backed by **$15.60B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `461,132,454` | N/A | Active |
| Block Height | `439,161,372` | N/A | Active |
| Current Epoch | `1067` (43.62% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,547.3 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `2,000.2` / `1,030.2 TPS` | N/A | Measured |
| Slot Duration | `211.3 ms` | ~400.0 ms | Normal |
| Total Transactions | `563,645,917,198` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 665 nodes
- **Delinquent Validators:** 25 nodes (3.62% delinquency rate)
- **Total Active Stake:** 436,976,346.73 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `CcaHc2L4...BzoTN1` | 17,099,112.8 SOL | 3.91% | 7% |
| #2 | `he1iusun...PauBtk` | 16,646,121.3 SOL | 3.81% | 0% |
| #3 | `3N7s9zXM...eWiD5g` | 12,588,035.1 SOL | 2.88% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,881,430.5 SOL | 2.49% | 0% |
| #5 | `CatzoSMU...gZDiqb` | 9,721,917.6 SOL | 2.23% | 5% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$102.46` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$60.43B` | 589.8M SOL circulating |
| 24h DEX Trading Volume | `$1.73B` | -13.25% delta |
| Total DeFi TVL | `$5.80B` | +0.46% delta |
| Circulating Stablecoins | `$15.60B` | USD: $15.52B, CAD: $1,447 |
| Median Transaction Fee | `$0.00102` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

✅ **All Systems Nominal.** Zero telemetry anomalies detected across latency, throughput, validator delinquency, TVL, and spot price bounds.

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
