from typing import Annotated, AsyncGenerator
from aiohttp import ClientSession
from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from api.repositories.user_repository import UserRepository
from api.services.auth_service import AuthService
from api.services.imei_service import IMEIService


async def get_db_session(
    request: Request,
) -> AsyncGenerator[AsyncSession, None]:
    session = await request.app.state.db_connection.get_session()
    try:
        yield session
    finally:
        await session.close()


async def get_client_session():
    async with ClientSession() as session:
        yield session


async def get_imei_service(session: ClientSession = Depends(get_client_session)):
    return IMEIService(session=session)


async def get_auth_service(session=Depends(get_db_session)):
    return AuthService(repository=UserRepository(session=session))


async def check_token(
    request: Request, 
    auth_service: Annotated[AuthService, Depends(get_auth_service)]
):
    request = await request.json()
    return await auth_service.check_token(request.get("token"))
