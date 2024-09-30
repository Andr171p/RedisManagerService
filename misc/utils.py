import datetime


def calculate_timeout(
        hour: int, minute: int, second: int, microsecond: int
) -> int:
    now = datetime.datetime.now()
    future = now.replace(
        hour=hour,
        minute=minute,
        second=second,
        microsecond=microsecond
    )
    if future <= now:
        future += datetime.timedelta(days=1)
    timeout = int((future - now).total_seconds())
    return timeout