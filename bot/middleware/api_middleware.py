from typing import Any, Awaitable, Callable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update
from aiohttp import ClientSession

from api.api_requests import APIRequests
from infrastructure.config import WHITE_LIST


class APIMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any]
    ) -> Any:
        if event.message.from_user.username not in WHITE_LIST:
            return await event.message.answer(text="У вас нет доступа к боту")
        async with ClientSession() as session:
            data["requests"] = APIRequests(session=session)
            return await handler(event, data)