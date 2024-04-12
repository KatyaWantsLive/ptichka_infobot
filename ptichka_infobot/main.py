import logging
import asyncio

from app.handlers.main import router
from loader import bot, dp, router
from app.db.models import async_main
from app.handlers.Contact import router
from app.handlers.rules import router
from app.handlers.about_us import router

async def main():
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Навернулась шарманка')
