from redis import Redis
from redis import asyncio as aioredis


class RedisConnection:
    _redis = None

    def __init__(self, url: str) -> None:
        self._url = url

    async def connect(self) -> Redis:
        self._redis = await aioredis.from_url(self._url)
        return self._redis

    async def close(self) -> None:
        await self._redis.close()
