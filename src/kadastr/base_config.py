from typing import AsyncGenerator

from httpx import AsyncClient

from src.kadastr import config


async def get_async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(base_url=config.EXTERNAL_API) as client:
        yield client
