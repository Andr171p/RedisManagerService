from redis import Redis

from storage.connection import RedisConnection
from storage.logs import RedisLogs

from loguru import logger


class RedisManager(RedisConnection):
    @staticmethod
    async def keys(redis: Redis) -> list:
        keys = await redis.keys('*')
        logger.info(RedisLogs.KEYS_LOG.format(keys=keys))
        return keys

    async def clear(self) -> None:
        redis = await self.connect()
        keys = await self.keys(redis=redis)
        try:
            await redis.delete(*keys)
            logger.info(RedisLogs.SUCCESSFULLY_CLEAR_LOG)
        except Exception as _ex:
            logger.warning(_ex)
        finally:
            await self.close()
