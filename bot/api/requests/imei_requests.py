from aiohttp import ClientSession

from api.requests.base import BaseRequests
from dto.imei_dto import IMEICheckErrorModel, IMEICheckModel, IMEICheckResponse
from infrastructure.config import API_TOKEN, API_URL


class IMEIRequests(BaseRequests):
    async def check_imei(self, imei: str) -> IMEICheckResponse | IMEICheckErrorModel:
        data = IMEICheckModel(imei=imei, token=API_TOKEN)
        async with self.session.post(
            url=f"{API_URL}/imei/check", 
            json=data.model_dump(),
            ssl=False
        ) as response:
            try:
                res = await response.json()
                if response.status != 200:
                    return IMEICheckErrorModel(**res)
                return IMEICheckResponse(**res)
            except Exception as e:
                return IMEICheckErrorModel(message=str(e))