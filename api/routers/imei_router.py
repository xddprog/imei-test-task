from typing import Annotated
from fastapi import APIRouter, Depends

from api.dto.imei_dto import IMEICheckModel, IMEICheckResponse
from api.infrastructure.dependencies import get_imei_service
from api.services.imei_service import IMEIService
from bot.dto.imei_dto import IMEICheckErrorModel


router = APIRouter()


@router.post("/check")
async def check_imei(
    form: IMEICheckModel,
    imei_service: Annotated[IMEIService, Depends(get_imei_service)]
) -> IMEICheckResponse | IMEICheckErrorModel:
    return await imei_service.check_imei(form)