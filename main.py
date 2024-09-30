import asyncio

from service.worker import start


if __name__ == "__main__":
    asyncio.run(start())
