import logging
import asyncio

from aiogram import Bot, Dispatcher

from middleware.api_middleware import APIMiddleware
from infrastructure.config import BOT_TOKEN
from keyboards.bot_commands import set_bot_commands
from handlers import all_handlers_router


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    await set_bot_commands(bot)
    dp.include_router(all_handlers_router)

    dp.update.middleware(APIMiddleware())
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
