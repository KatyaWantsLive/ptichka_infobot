import logging
import asyncio

from loader import bot, dp
from app.db.models import async_main

from app.handlers.router import include_routers

async def main():
    await async_main()
    include_routers()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Навернулась шарманка')
