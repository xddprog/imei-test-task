from pydantic import BaseModel


class AuthUserModel(BaseModel):
    username: str
    password: str


class GetTGTokenModel(BaseModel):
    secret_key: str