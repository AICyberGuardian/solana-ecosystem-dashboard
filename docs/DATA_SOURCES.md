# Data Sources & Provenance Specification

Every metric ingested by the Solana Ecosystem Intelligence Suite is collected using zero paid API keys and public endpoints.

---

## 1. On-Chain Solana RPC Telemetry

All direct on-chain state queries connect to public Solana JSON-RPC 2.0 endpoints. Failover rotates automatically across:
1. `https://api.mainnet-beta.solana.com`
2. `https://solana-rpc.publicnode.com`
3. `https://rpc.ankr.com/solana`

### Collected RPC Methods:
- `getHealth`: Returns cluster health status (`ok`, `behind`, or HTTP error).
- `getEpochInfo`: Extracts current epoch, slot index within epoch, total slots per epoch (432,000), absolute slot number, block height, and cumulative transaction count.
- `getRecentPerformanceSamples(60)`: Fetches 60 consecutive 1-minute performance intervals. Calculates:
  - Exact current TPS: `numTransactions / samplePeriodSecs`
  - 1-hour average, peak, and minimum TPS.
  - Mean slot generation interval in milliseconds: `(samplePeriodSecs / numSlots) * 1000`.
- `getVoteAccounts`: Returns all current active and delinquent validator vote accounts. Computes:
  - Total active and delinquent validator count.
  - Cluster delinquency rate percentage.
  - Total active stake (lamports converted to SOL).
  - Accurate **Nakamoto Coefficient**: The minimum number of validators needed to collude to control >33.33% of total active stake and halt consensus.
  - Top 10 validators by active stake and commission rates.
- `getSupply`: Returns total, circulating, and non-circulating SOL supplies.

---

## 2. DeFi, TVL & Liquidity Metrics (DeFiLlama)

DeFi metrics are ingested keylessly from DeFiLlama's public APIs:
- `/v2/chains`: Global chain TVL metrics; filters for Solana.
- `/v2/historicalChainTvl/Solana`: Full daily historical TVL series. Extracts 30-day trendline and computes precise 24-hour and 7-day percentage changes.
- `/overview/dexs/solana`: Solana decentralized exchange trading volumes (24-hour total, 7-day total, 24-hour volume percentage change).
- `/stablecoinchains`: Circulating stablecoin supply broken down by currency peg (USDC, USDT, EURC, CAD stablecoins).
- `/protocols`: Top protocols deployed on Solana filtered and sorted by TVL (Sanctum, Kamino, Raydium, Jito, Marinade).

---

## 3. Spot Market & Real Economic Value (Binance & Coinbase)

Spot pricing and market valuation are sourced via public ticker endpoints:
- `https://api.binance.com/api/v3/ticker/24hr?symbol=SOLUSDT`: 24-hour spot price, 24-hour price change percentage, 24-hour high/low, and 24-hour quote volume.
- Failover: `https://api.coinbase.com/v2/prices/SOL-USD/spot`.
- Market Cap is dynamically derived: `SOL_Spot_Price * Circulating_Supply_SOL`.
- Real Economic Value / Median Tx Fee: Computed from baseline transaction fee schedules (0.00001 SOL) multiplied by spot price.
