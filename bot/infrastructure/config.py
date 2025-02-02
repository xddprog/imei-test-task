import asyncio
from aiohttp import ClientSession
from environs import Env


async def get_api_token(secret_key: str):
    async with ClientSession() as session:
        async with session.post(
            url=f"{API_URL}/auth/login/tg",
            json={"secret_key": secret_key}
        ) as response:
            res = await response.json()
            return res


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
WHITE_LIST = env.list("WHITE_LIST", subcast=int, default=[])
API_URL = env.str("API_URL")

API_TOKEN = asyncio.run(get_api_token(env.str("SECRET_KEY")))
