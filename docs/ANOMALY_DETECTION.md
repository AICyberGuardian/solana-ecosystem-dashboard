# Anomaly Detection & Health Scoring Engine

The suite implements autonomous multi-factor anomaly detection and a composite 0-100 Ecosystem Health Score to transform raw metrics into actionable operational alerts.

---

## 1. Anomaly Detection Rules

The `AnomalyDetector` evaluates seven distinct operational signals across three severity classifications (`CRITICAL`, `WARNING`, `INFO`):

| Signal | Metric | Threshold Condition | Severity | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Node Health** | RPC Cluster Status | Status != `'ok'` | `CRITICAL` / `WARNING` | RPC node consensus loss or divergence. |
| **Throughput Drop** | Current TPS vs 1h Average | Delta < -25.0% | `WARNING` | Block space underutilization or transaction propagation delay. |
| **Throughput Spike** | Current TPS vs 1h Average | Delta > +60.0% | `INFO` | High network demand event or surge in program execution. |
| **Slot Latency** | Mean Slot Time | Latency > 550.0 ms | `WARNING` (>700ms `CRITICAL`) | Consensus lag; target slot time is ~400 ms. |
| **Delinquency Surge** | Delinquent Validator % | Rate > 5.0% | `WARNING` (>10% `CRITICAL`) | Large validator cohort offline or skipping vote transactions. |
| **Nakamoto Shift** | Nakamoto Coefficient | Value < 16 | `WARNING` | Stake centralization warning; cluster security requires distributed voting power. |
| **TVL Volatility** | 24h TVL Change % | Absolute Delta > 10.0% | `WARNING` / `INFO` | Sharp liquidity inflow or rapid capital flight. |
| **Price Volatility** | 24h SOL Price Delta | Absolute Delta > 12.0% | `WARNING` / `INFO` | Macro volatility influencing validator staking margins and fee dynamics. |

---

## 2. Composite Ecosystem Health Score (0 - 100)

The `HealthScoreEngine` grades the Solana cluster across four balanced operational pillars, allocating up to 25 points per pillar:

### Pillar 1: Network Liveness & Latency (Max 25 pts)
- RPC node health status == `ok`: **15 pts** (behind: 8 pts, error: 0 pts)
- Mean slot time <= 420 ms: **10 pts** (<= 480 ms: 7 pts, <= 550 ms: 4 pts, > 550 ms: 0 pts)

### Pillar 2: Throughput & Capacity (Max 25 pts)
- Current TPS >= 3,500: **15 pts** (>= 2,500: 12 pts, >= 1,500: 8 pts, >= 500: 4 pts)
- TPS stability (current vs 1h rolling avg within 20%): **10 pts** (within 40%: 6 pts, otherwise: 3 pts)

### Pillar 3: Validator Security & Decentralization (Max 25 pts)
- Nakamoto coefficient >= 18: **15 pts** (>= 16: 12 pts, >= 14: 8 pts, < 14: 4 pts)
- Delinquency rate < 2.0%: **10 pts** (< 4.0%: 7 pts, < 6.0%: 4 pts, >= 6.0%: 0 pts)

### Pillar 4: DeFi & Economic Vitality (Max 25 pts)
- Total DeFi TVL >= $5.0B: **10 pts** (>= $3.0B: 7 pts, >= $1.0B: 4 pts)
- Circulating Stablecoins >= $10.0B: **10 pts** (>= $5.0B: 7 pts, >= $2.0B: 4 pts)
- 24h DEX Volume >= $1.0B: **5 pts** (>= $500M: 3 pts)

### Rating Brackets:
- **90 - 100:** `OPTIMAL` (Vibrant green `#14F195`)
- **75 - 89:** `HEALTHY` (Teal `#00FFA3`)
- **60 - 74:** `MODERATE` (Amber `#FFA500`)
- **< 60:** `DEGRADED` (Red `#EF4444`)
