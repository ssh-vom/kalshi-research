import httpx
import asyncio
from typing import Any
from collections.abc import AsyncIterator
from config.settings import KALSHI_API_KEY, KALSHI_API_URL

JsonObject = dict[str, Any]
JsonList = list[JsonObject]


class KalshiClient:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {KALSHI_API_KEY}"}
        self.base_url = KALSHI_API_URL
        self.client = httpx.AsyncClient(timeout=10)

    async def list_markets(self) -> JsonList:
        data = await self._get("/v2/markets")
        return data.get("markets", [])

    async def get_market(self, market_id: int) -> JsonObject:
        return await self._get(f"/v2/markets/{market_id}")

    async def list_events(self) -> JsonList:
        data = await self._get("/v2/events")
        return data.get("events", [])

    async def _get(self, path: str, params: dict | None = None) -> Any:
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = await self.client.get(url, headers=None, params=params)
        response.raise_for_status()
        return response.json()

    async def _paginate(
        self,
        path: str,
        data_key: str,
        params: dict | None = None,
        limit: int = 100,
    ) -> AsyncIterator[JsonObject]:
        cursor: str | None = None

        while True:
            query = dict(params or {})
            query["limit"] = limit
            if cursor:
                query["cursor"] = cursor

            await asyncio.sleep(4)

            data = await self._get(path, params=query)

            items = data.get(data_key, [])
            for item in items:
                yield item

            cursor = data.get("cursor")
            if not cursor:
                break

        return

    async def list_all_markets(self) -> JsonList:
        markets: JsonList = []
        async for market in self._paginate(
            "/v2/markets",
            data_key="markets",
        ):
            markets.append(market)
            print(market)
            print("\n")

        return markets

    async def close(self):
        await self.client.aclose()


if __name__ == "__main__":
    client = KalshiClient()
    markets = asyncio.run(client.list_all_markets())
