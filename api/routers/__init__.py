from fastapi import APIRouter, Depends
from api.infrastructure.dependencies import check_token
from api.routers.auth_router import router as auth_router
from api.routers.imei_router import router as imei_router


all_routers = APIRouter(prefix="/api/v1")
PROTECTED = Depends(check_token)


all_routers.include_router(imei_router, tags=["IMEI"], prefix="/imei", dependencies=[PROTECTED])
all_routers.include_router(auth_router, tags=["AUTH"], prefix="/auth")