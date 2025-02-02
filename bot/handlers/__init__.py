from aiogram import Router
from handlers.imei_handler import router as imei_router
from handlers.bot_commands import router as bot_commands_router


all_handlers_router = Router()


all_handlers_router.include_router(bot_commands_router)
all_handlers_router.include_router(imei_router)
