from typing import Annotated
from fastapi import APIRouter, Depends

from api.dto.auth import AuthUserModel, GetTGTokenModel
from api.infrastructure.dependencies import get_auth_service
from api.services.auth_service import AuthService


router = APIRouter()


@router.post("/login/tg")
async def login_tg(
    form: GetTGTokenModel, 
    auth_service: Annotated[AuthService, Depends(get_auth_service)]
) -> str:
    return await auth_service.get_api_token_from_tg(form)


@router.post("/register")
async def register(
    form: AuthUserModel, 
    auth_service: Annotated[AuthService, Depends(get_auth_service)]
) -> str:
    return await auth_service.register_user(form)


@router.post("/login")
async def login(
    form: AuthUserModel, 
    auth_service: Annotated[AuthService, Depends(get_auth_service)]
) -> str:
    return await auth_service.login_user(form)