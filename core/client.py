import httpx
from typing import Any
from config.settings import KALSHI_API_KEY, KALSHI_API_URL

JsonObject = dict[str, Any]
JsonList = list[JsonObject]


class KalshiClient:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {KALSHI_API_KEY}"}
        self.base_url = KALSHI_API_URL
        self.client = httpx.AsyncClient(timeout=10)

    async def list_markets(self) -> JsonList:
        return await self._get("/v2/markets")

    async def get_market(self, market_id: int) -> JsonObject:
        return await self._get(f"/v2/markets/{market_id}")

    async def list_events(self) -> JsonList:
        return await self._get("/v2/events")

    async def _get(self, path) -> Any:
        url = f"{self.base_url}{path}"
        request = await self.client.get(url, headers=None)
        request.raise_for_status()
        return request.json()

    async def close(self):
        await self.client.aclose()
