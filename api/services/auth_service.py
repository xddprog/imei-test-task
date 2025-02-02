from uuid import uuid4
from api.database.models.user import User
from api.dto.auth import AuthUserModel, GetTGTokenModel
from api.errors.auth_errors import AccessDenied
from api.errors.user_errors import UserAlreadyRegistered, UserNotFound
from api.infrastructure.config import SECRET_KEY, TG_API_TOKEN
from api.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def _get_by_username(self, username: str) -> User:
        return await self.repository.get_by_attributes(
            (self.repository.model.username, username),
            one_or_none=True
        )
    
    async def _get_by_token(self, token: str) -> User:
        return await self.repository.get_by_attributes(
            (self.repository.model.token, token),
            one_or_none=True
        )

    async def get_api_token_from_tg(self, form: GetTGTokenModel) -> str:
        if form.secret_key != SECRET_KEY:
            raise AccessDenied
        return TG_API_TOKEN
    
    async def register_user(self, form: AuthUserModel) -> str:
        user_exist = await self._get_by_username(form.username)
        if user_exist:
            raise UserAlreadyRegistered
        
        token = str(uuid4())
        await self.repository.add_item(
            username=form.username,
            password=form.password,
            token=token
        )
        return token

    async def login_user(self, form: AuthUserModel) -> str:
        user_exist = await self._get_by_username(form.username)
        if not user_exist:
            raise UserNotFound
        return user_exist.token
    
    async def check_token(self, token: str) -> None:
        if token == TG_API_TOKEN:
            return
        user = await self._get_by_token(token)
        if not user:
            raise AccessDenied