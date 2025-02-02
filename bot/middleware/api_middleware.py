from typing import Any, Awaitable, Callable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update
from aiohttp import ClientSession

from api.api_requests import APIRequests


class APIMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any]
    ) -> Any:
        async with ClientSession() as session:
            data["requests"] = APIRequests(session=session)
            return await handler(event, data)