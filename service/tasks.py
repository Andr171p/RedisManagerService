from storage.settings import RedisSettings
from storage.manager import RedisManager


redis_manager = RedisManager(url=RedisSettings.REDIS_PUBLIC_URL)


async def task() -> None:
    await redis_manager.clear()
