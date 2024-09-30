from service.tasks import task
from service.scheduler import Scheduler
from service.settings import ServiceSettings

from misc.utils import calculate_timeout


async def start() -> None:
    timeout = calculate_timeout(
        hour=ServiceSettings.HOUR,
        minute=ServiceSettings.MINUTE,
        second=ServiceSettings.SECOND,
        microsecond=ServiceSettings.MICROSECOND
    )
    scheduler = Scheduler(
        timeout=timeout,
        task=task
    )
    await scheduler.scheduler()
