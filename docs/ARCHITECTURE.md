# Solana Ecosystem Intelligence: Architectural Overview

## 1. Design Philosophy

The **Solana Ecosystem Auto-Updating Report & Interactive Bento Dashboard** is built around three core engineering invariants:

1. **Zero External Paid Dependencies & Zero API Keys:** Operates strictly on Python 3.10+ standard library (`urllib.request`, `json`, `math`, `time`, `http.server`) combined with free, public, keyless infrastructure (Solana JSON-RPC 2.0 endpoints, DeFiLlama public aggregates, Binance and Coinbase public tickers).
2. **Resilience & Failover:** Network requests to Solana RPC nodes feature round-robin failover across multiple public providers (`api.mainnet-beta.solana.com`, `solana-rpc.publicnode.com`, `rpc.ankr.com/solana`) to ensure uninterrupted telemetry even during rate limits or localized outages.
3. **Multi-Format Publication:** From a single telemetry harvest, the engine produces:
   - An interactive dark-mode **Bento UI HTML Dashboard** (`output/dashboard.html`).
   - An executive **Markdown Report** (`output/report.md`).
   - A structured **JSON Data Payload** (`output/data.json`).

---

## 2. Component Pipeline

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
|   - Live Indicator & Dial         - Prose-Craft Compliant        Payload        |
+---------------------------------------------------------------------------------+
```

---

## 3. Directory Layout

```
solana-ecosystem-dashboard/
|-- src/
|   |-- collectors/
|   |   |-- rpc_collector.py       # Solana JSON-RPC 2.0 client with failover
|   |   |-- defillama_collector.py # TVL, DEX volume, stablecoins, protocols
|   |   |-- market_collector.py    # Spot price, market cap, fee estimation
|   |-- analysis/
|   |   |-- anomaly_detector.py    # Statistical & threshold anomaly engine
|   |   |-- health_score.py        # Composite 0-100 ecosystem health index
|   |-- generators/
|   |   |-- html_generator.py      # Bento UI HTML renderer
|   |   |-- markdown_generator.py  # Markdown status report generator
|   |   |-- json_generator.py      # JSON telemetry serializer
|   |-- config.py                  # Global configurations & thresholds
|   |-- cli.py                     # CLI parser, daemon loop, and HTTP server
|-- templates/
|   |-- dashboard.html             # Bento UI HTML5 template with Chart.js
|-- output/
|   |-- dashboard.html             # Live rendered interactive dashboard
|   |-- report.md                  # Generated Markdown report
|   |-- data.json                  # Generated JSON data
|-- tests/
|   |-- test_collectors.py         # Unit tests for network collectors
|   |-- test_analysis.py           # Unit tests for scoring & anomaly detection
|   |-- test_generators.py         # Unit tests for artifact generators
|-- docs/
|   |-- ARCHITECTURE.md            # System architecture (this file)
|   |-- DATA_SOURCES.md            # Detailed data dictionary & provenance
|   |-- ANOMALY_DETECTION.md       # Statistical rules & anomaly thresholds
|-- run.py                         # Single executable CLI entrypoint
|-- pyproject.toml                 # Standard Python packaging metadata
|-- requirements.txt               # Requirements manifest
|-- LICENSE                        # MIT License
`-- README.md                      # Project documentation & runbook
```
