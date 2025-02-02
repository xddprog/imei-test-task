from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    message_text = (
        "Добро пожаловать в бота!"
        "Чтоб проверить imei просто отправьте его боту"
    )
    await message.answer(message_text)
    