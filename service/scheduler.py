import asyncio

from service.logs import ServiceLog

from loguru import logger


class Scheduler:
    def __init__(self, timeout: int, task: callable) -> None:
        self._timeout = timeout
        self._task = task

    async def scheduler(self) -> None:
        logger.info(ServiceLog.START_LOG)
        while True:
            await asyncio.sleep(self._timeout)
            logger.info(ServiceLog.RUN_TASK_LOG)
            await self._task()
