# Solana Ecosystem Status & Telemetry Report
**Generated:** `2026-11-06T13:54:15Z` | **Health Score:** `76.0/100` (HEALTHY) | **Zero API Keys**

---

## 1. Executive Summary

The Solana mainnet cluster is operating under **HEALTHY** parameters with a composite health rating of **76.0/100**.
Current network throughput stands at **1,454.8 TPS** (1-hour average: 1,518.4 TPS) with an average slot generation interval of **213.9 ms**.
Total value locked across Solana DeFi protocols totals **$5.31B** (-3.90% 24h delta), backed by **$14.54B** in on-chain stablecoin liquidity.

---

## 2. Network Performance & Consensus

| Metric | Current Value | Baseline / Target | Status |
| :--- | :--- | :--- | :--- |
| Cluster Health | `ok` | `ok` | Normal |
| Current Slot | `466,133,534` | N/A | Active |
| Block Height | `444,152,971` | N/A | Active |
| Current Epoch | `1079` (1.28% complete) | 432,000 slots | In Progress |
| Throughput (Current) | `1,454.8 TPS` | > 2,500 TPS | Healthy |
| Throughput (1h Peak / Min) | `3,147.2` / `1,189.4 TPS` | N/A | Measured |
| Slot Duration | `217.4 ms` | ~400.0 ms | Normal |
| Total Transactions | `565,511,577,766` | Monotonic | Active |

---

## 3. Validator Health & Decentralization

- **Active Validators:** 648 nodes
- **Delinquent Validators:** 48 nodes (6.90% delinquency rate)
- **Total Active Stake:** 431,380,481.64 SOL
- **Nakamoto Coefficient:** `16` minimum validators required to compromise consensus (>33.33% total active stake)

### Top 5 Validators by Active Stake

| Rank | Node / Vote Account | Active Stake (SOL) | Stake Share | Commission |
| :--- | :--- | :--- | :--- | :--- |
| #1 | `CcaHc2L4...BzoTN1` | 17,039,555.6 SOL | 3.95% | 7% |
| #2 | `he1iusun...PauBtk` | 16,722,208.5 SOL | 3.88% | 0% |
| #3 | `3N7s9zXM...eWiD5g` | 13,017,562.5 SOL | 3.02% | 0% |
| #4 | `8GbwASqd...GJF8iD` | 10,436,419.7 SOL | 2.42% | 0% |
| #5 | `CatzoSMU...gZDiqb` | 9,531,945.8 SOL | 2.21% | 5% |

---

## 4. Economic Indicators & DeFi Metrics

| Indicator | Value (USD) | 24h Change / Details |
| :--- | :--- | :--- |
| SOL Spot Price | `$90.22` | +0.00% (Source: Coinbase) |
| Estimated Circulating Market Cap | `$53.26B` | 590.3M SOL circulating |
| 24h DEX Trading Volume | `$2.20B` | -7.85% delta |
| Total DeFi TVL | `$5.31B` | -3.90% delta |
| Circulating Stablecoins | `$14.54B` | USD: $14.46B, CAD: $1,441 |
| Median Transaction Fee | `$0.00090` | ~0.000010 SOL |

---

## 5. Anomaly Detection Feed

| Severity | Metric | Current Value | Threshold | Details |
| :--- | :--- | :--- | :--- | :--- |
| `WARNING` | **Validator Delinquency Rate** | `6.90%` | `<= 5.0%` | 6.90% of validators are currently delinquent or missing votes. |

---

## 6. Architecture & Data Provenance

- **On-Chain Extraction:** Direct Solana JSON-RPC 2.0 endpoints with round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **DeFi & Liquidity:** Keyless public DeFiLlama protocol and stablecoin chain aggregates.
- **Market Data:** Public Binance & Coinbase spot ticker endpoints.
- **Dependencies:** Pure Python standard library (`urllib.request`, `json`, `math`, `time`). Zero paid API keys.
