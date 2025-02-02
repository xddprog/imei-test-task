from fastapi import FastAPI

from api.database.connection import DatabaseConnection
from api.routers import all_routers


async def lifespan(app):
    app.state.db_connection = await DatabaseConnection()()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(all_routers)