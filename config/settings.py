import os
from dotenv import load_dotenv

load_dotenv()

KALSHI_API_KEY = os.getenv("KALSHI_API_KEY")
KALSHI_API_URL = "https://api.kalshi.com/v1"

SNAPSHOT_INTERVAL = int(os.getenv("SNAPSHOT_INTERVAL", 5))
