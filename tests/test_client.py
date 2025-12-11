import pytest
import respx
from httpx import Response
from core.client import KalshiClient


@pytest.mark.asyncio
@respx.mock
async def test_get_markets_success():
    mocked_route = respx.get("https://api.kalshi.com/v1/markets").mock(
        return_value=Response(
            200, json={"markets": [{"id": "GDP-2024", "title": "US GDP"}]}
        )
    )

    client = KalshiClient()

    result = await client.list_markets()

    assert mocked_route.called, "The API was never called"
    assert "markets" in result
    await client.close()
