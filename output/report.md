# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-21T12:55:10Z` | **Health Score:** `80.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **80.0/100**.
Current network throughput stands at **1,020.7 TPS** (1-hour average: 1,194.1 TPS) with an average slot generation interval of **214.8 ms**.
Total value locked across Solana DeFi protocols totals **$4.52B** (-4.00% 24h delta), backed by **$13.19B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `472,146,472` | N/A | Active |
| Block Height | `450,160,430` | N/A | Active |
| Current Epoch | `1092` (93.16% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,020.7 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `2,122.5` / `851.9 TPS` | N/A | Measured |
| Slot Duration | `219.0 ms` | ~400.0 ms | Normal |
| Total Transactions | `567,733,280,202` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 662 nodes
- **Delinquent Validators:** 23 nodes (3.36% delinquency rate)
- **Total Active Stake:** 428,912,356.00 SOL
- **Nakamoto Coefficient:** `17` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `he1iusun...PauBtk` | 17,041,637.9 SOL | 3.97% | 0% |
| #2 | `CcaHc2L4...BzoTN1` | 16,354,101.2 SOL | 3.81% | 7% |
| #3 | `3N7s9zXM...eWiD5g` | 12,422,891.2 SOL | 2.90% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,309,120.9 SOL | 2.40% | 0% |
| #5 | `51JBzSTU...zgUNAm` | 9,779,397.3 SOL | 2.28% | 10% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$69.13` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$40.92B` | 591.9M SOL circulating |
| 24h DEX Trading Volume | `$1.88B` | -1.02% delta |
| Total DeFi TVL | `$4.52B` | -4.00% delta |
| Circulating Stablecoins | `$13.19B` | USD: $13.10B, CAD: $1,438 |
| Median Transaction Fee | `$0.00069` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

✅ **All Systems Nominal.** Zero telemetry anomalies detected across latency, throughput, validator delinquency, TVL, and spot price bounds.

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
