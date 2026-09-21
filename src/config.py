import os
from typing import List

# Default Public Solana JSON-RPC endpoints (ordered by priority)
DEFAULT_PUBLIC_RPCS: List[str] = [
    "https://api.mainnet-beta.solana.com",
    "https://solana-rpc.publicnode.com",
    "https://rpc.ankr.com/solana"
]

# External Data APIs (Keyless)
DEFILLAMA_BASE_URL: str = "https://api.llama.fi"
DEFILLAMA_STABLES_URL: str = "https://stablecoins.llama.fi"
BINANCE_TICKER_URL: str = "https://api.binance.com/api/v3/ticker/24hr?symbol=SOLUSDT"
COINBASE_SPOT_URL: str = "https://api.coinbase.com/v2/prices/SOL-USD/spot"

# Operational Thresholds for Anomaly Detection
TPS_DROP_THRESHOLD_PCT: float = 25.0
SLOT_TIME_MAX_MS: float = 550.0
DELINQUENCY_MAX_PCT: float = 5.0
TVL_CHANGE_MAX_PCT: float = 10.0
PRICE_CHANGE_MAX_PCT: float = 12.0

# Output Paths
DEFAULT_OUTPUT_DIR: str = "output"
DEFAULT_JSON_OUTPUT: str = os.path.join(DEFAULT_OUTPUT_DIR, "data.json")
DEFAULT_MD_OUTPUT: str = os.path.join(DEFAULT_OUTPUT_DIR, "report.md")
DEFAULT_HTML_OUTPUT: str = os.path.join(DEFAULT_OUTPUT_DIR, "dashboard.html")

# Daemon & Server Defaults
DEFAULT_REFRESH_INTERVAL_SEC: int = 300  # 5 minutes
DEFAULT_HTTP_PORT: int = 8080
DEFAULT_TIMEOUT_SEC: int = 15
