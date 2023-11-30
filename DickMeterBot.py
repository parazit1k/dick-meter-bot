import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from Handlers.Commands.start import start_router
from Handlers.Commands.metr import dick_router

TOKEN = ""


async def main() -> None:
    dp = Dispatcher()

    dp.include_routers(
        start_router,
        dick_router
    )

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
