from aiogram import F, Router
from aiogram.types import Message

from api.api_requests import APIRequests
from filters.imei_filters import IsValidIMEI
from dto.imei_dto import IMEICheckErrorModel


router = Router()


@router.message(IsValidIMEI())
async def check_imei(message: Message, requests: APIRequests):
    check_imei = await requests.imei_requests.check_imei(imei=message.text)
    if isinstance(check_imei, IMEICheckErrorModel):
        await message.answer(text=check_imei.detail)
    else:
        message_text = "\n".join([
            f"{key}: {value}" 
            for key, value in check_imei.model_dump().items()
        ])
        await message.reply(text=message_text)


@router.message(~IsValidIMEI())
async def invalid_imei(message: Message):
    await message.answer(text="Неверный формат IMEI")