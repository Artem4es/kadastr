from typing import AsyncGenerator

from httpx import AsyncClient

from src.config import EXTERNAL_API


async def get_async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(base_url=EXTERNAL_API) as client:
        yield client
