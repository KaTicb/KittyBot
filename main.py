import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings
import asyncio

from utils import router as utils_router
from base_commands import router as base_router
from keyboards import router as callbacks_router

api_key = settings.api_key
dp = Dispatcher()

dp.include_routers(base_router, callbacks_router, utils_router, )


async def main():
    bot = Bot(token=api_key, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
