import os
from dotenv import load_dotenv

load_dotenv()

KALSHI_API_KEY = os.getenv("KALSHI_API_KEY")
KALSHI_API_URL = os.getenv(
    "KALSHI_API_URL", "https://api.elections.kalshi.com/trade-api"
)

SNAPSHOT_INTERVAL = int(os.getenv("SNAPSHOT_INTERVAL", 5))
