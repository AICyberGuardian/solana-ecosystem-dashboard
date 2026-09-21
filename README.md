# Solana Ecosystem Intelligence: Auto-Updating Report & Interactive Bento Dashboard

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dependencies: Zero](https://img.shields.io/badge/Dependencies-Zero-success.svg)](#zero-dependency-philosophy)
[![Solana Mainnet](https://img.shields.io/badge/Network-Solana%20Mainnet--Beta-14F195?logo=solana&logoColor=black)](https://solana.com)
[![Superteam Canada](https://img.shields.io/badge/Built%20for-Superteam%20Canada-FF0055)](https://superteam.fun)

An autonomous, zero-API-key ecosystem intelligence platform that harvests live on-chain Solana telemetry, aggregates DeFi liquidity metrics, executes real-time anomaly detection, computes a 0–100 Ecosystem Health Score, and renders an interactive dark-mode Bento UI dashboard alongside executive Markdown and structured JSON reports.

Designed and engineered for **Superteam Canada**.

---

## Key Highlights

- **Zero External Paid Dependencies & Zero API Keys:** Built on the pure Python standard library. Requires no paid subscriptions, Dune API keys, or CoinGecko keys.
- **Direct On-Chain Telemetry:** Queries Solana JSON-RPC 2.0 nodes with automatic round-robin failover (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`).
- **Comprehensive Coverage:**
  - **Performance:** Live TPS, 1-hour average, peak throughput, slot generation duration, epoch progress, total transaction count.
  - **Decentralization:** Active vs. delinquent validator counts, total active stake (SOL), top 10 validators by stake and commission, and an exact **Nakamoto coefficient** calculation.
  - **DeFi & Liquidity:** Total Value Locked (TVL), 30-day historical TVL trajectory, 24h/7d DEX trading volumes, stablecoin market cap (with Canadian dollar stablecoin tracking), and top Solana protocols.
  - **Economic Indicators:** SOL spot price, 24-hour price change, circulating market capitalization, and median transaction fee estimation.
- **Autonomous Anomaly Detection:** Real-time multi-factor surveillance flagging throughput drops, slot time deceleration, validator delinquency surges, and TVL/price swings.
- **Ecosystem Health Score (0–100):** Deterministic multi-pillar scoring system evaluating Network Liveness, Throughput & Stability, Validator Security, and DeFi Vitality.
- **Tri-Format Output Generation:**
  1. `output/dashboard.html`: Self-contained Bento UI dark-mode interactive dashboard with responsive Chart.js visualizations.
  2. `output/report.md`: Executive summary status report written in rigorous technical prose.
  3. `output/data.json`: Structured machine-readable telemetry snapshot.
- **Configurable Automation:** One-shot generation (`--generate`), background daemon loop (`--daemon --interval 300`), and built-in zero-dependency HTTP server (`--serve --port 8080`).

---

## Interactive Bento UI Dashboard Preview

The generated dashboard (`output/dashboard.html`) renders an Apple Bento-inspired interface themed in Solana dark-mode (`#07090E` background, `#121826` glassmorphic cards, `#14F195` green and `#9945FF` purple accents):

- **Health Dial:** Circular gauge presenting the 0–100 Ecosystem Health Score with breakdown bars across the 4 operational pillars.
- **Throughput Sparkline:** Live 30-sample rolling TPS curve.
- **Consensus Progress:** Animated epoch completion meter and real-time slot generation latency.
- **TVL Trajectory Chart:** Responsive 30-day historical chart displaying TVL momentum.
- **Validator Stake Donut:** Visual distribution comparing top 5 validator voting power against the remaining cluster.
- **Autonomous Anomaly Feed:** Real-time badge and operational alerts table.

---

## Architecture

```
+---------------------------------------------------------------------------------+
|                               DATA INGESTION                                    |
|                                                                                 |
|  [Solana Public RPCs]       [DeFiLlama Public API]      [Exchanges (Binance/CB)]|
|   - getHealth                - /v2/chains (TVL)          - SOL/USDT Ticker      |
|   - getEpochInfo             - /v2/historicalChainTvl    - 24h Vol & Deltas     |
|   - getRecentPerfSamples     - /overview/dexs/solana     - Median Tx Fee Est.   |
|   - getVoteAccounts          - /stablecoins                                     |
|   - getSupply                - /protocols                                       |
+---------------------------------------+-----------------------------------------+
                                        |
                                        v
+---------------------------------------------------------------------------------+
|                              ANALYSIS & SCORING                                 |
|                                                                                 |
|  [HealthScoreEngine]                                 [AnomalyDetector]          |
|   - Network Liveness (25 pts)                         - TPS Drop/Spike Detector |
|   - Throughput & Stability (25 pts)                   - Slot Duration Drift     |
|   - Validator Security / Nakamoto (25 pts)            - Delinquency Surge Rate  |
|   - DeFi & Economic Vitality (25 pts)                 - TVL / Price Volatility  |
+---------------------------------------+-----------------------------------------+
                                        |
                                        v
+---------------------------------------------------------------------------------+
|                              OUTPUT GENERATION                                  |
|                                                                                 |
|  [HTMLGenerator]                 [MarkdownGenerator]          [JSONGenerator]   |
|   - Bento UI Dark Mode            - Executive Summary          - Machine-       |
|   - Chart.js Visualizations       - Markdown Tables              readable       |
|   - Live Indicator & Dial         - Technical Prose              Payload        |
+---------------------------------------------------------------------------------+
```

---

## Quickstart & Usage

### 1. Requirements
- Python 3.10 or higher.
- No third-party packages required to run!

### 2. Generate Reports Once
Run a single telemetry harvest and report generation:

```bash
python run.py --generate
```

Outputs will be generated immediately in the `output/` directory:
- `output/dashboard.html`
- `output/report.md`
- `output/data.json`

### 3. Launch Interactive Local Dashboard
To generate reports and start a local HTTP server to view the interactive dashboard in your browser:

```bash
python run.py --serve --port 8080
```
Then navigate to: `http://localhost:8080/dashboard.html`

### 4. Run Autonomous Background Daemon
To run continuously as an autonomous background daemon that refreshes data every 5 minutes (300 seconds):

```bash
python run.py --daemon --interval 300
```

To run the daemon with the local HTTP server simultaneously:

```bash
python run.py --daemon --interval 300 --serve --port 8080
```

---

## Verification & Testing

Execute the test suite verifying all collectors, anomaly detectors, scoring math, and report generators:

```bash
python -m unittest discover tests
```

Expected output:
```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.35s

OK
```

---

## Data Sources & Provenance

| Dimension | Primary Source | Protocol / Endpoint | Fallback |
| :--- | :--- | :--- | :--- |
| **Network & Consensus** | Solana Mainnet-Beta | JSON-RPC 2.0 (`api.mainnet-beta.solana.com`) | `solana-rpc.publicnode.com`, `rpc.ankr.com/solana` |
| **Validators & Nakamoto** | Solana Cluster | JSON-RPC `getVoteAccounts` | Automatic RPC failover |
| **DeFi TVL & DEX Volume** | DeFiLlama | `api.llama.fi/v2/chains`, `/overview/dexs/solana` | Built-in rolling cache |
| **Stablecoin Supply** | DeFiLlama Stablecoins | `stablecoins.llama.fi/stablecoinchains` | Local snapshot |
| **Market Pricing & Fees** | Binance Ticker | `api.binance.com/api/v3/ticker/24hr?symbol=SOLUSDT` | Coinbase Spot API (`api.coinbase.com`) |

---

## Anomaly Detection Rules

The anomaly engine evaluates telemetry continuously against baseline heuristics:

1. **RPC Health:** Flags any state where `getHealth` deviates from `ok`.
2. **Throughput Drops:** Alerts if current TPS is >25% below the 1-hour moving average.
3. **Slot Generation Lag:** Flags slot duration exceeding 550 ms (target: ~400 ms).
4. **Validator Delinquency:** Alerts if cluster delinquent validator rate exceeds 5.0%.
5. **Decentralization Drift:** Warns if Nakamoto coefficient dips below 16 validators.
6. **TVL / Price Volatility:** Detects 24-hour TVL shifts exceeding ±10% or SOL price swings exceeding ±12%.

---

## Documentation

- [System Architecture](docs/ARCHITECTURE.md)
- [Data Sources & Provenance](docs/DATA_SOURCES.md)
- [Anomaly Detection Specification](docs/ANOMALY_DETECTION.md)

---

## License

This project is licensed under the [MIT License](LICENSE).
Built with passion by **Nyxar Labs** for **Superteam Canada**.
