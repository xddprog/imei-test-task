from aiohttp import ClientSession

from api.dto.imei_dto import IMEICheckModel, IMEICheckResponse
from api.errors.imei_errors import IMEICheckError
from api.infrastructure.config import IMEI_CHECK_API_KEY, IMEI_CHECK_API_URL, SERVICE_ID


class IMEIService:
    def __init__(self, session: ClientSession):
        self.session = session

    async def check_imei(self, form: IMEICheckModel) -> IMEICheckResponse:
        async with self.session.post(
            url=f"{IMEI_CHECK_API_URL}/checks", 
            json={"deviceId": form.imei, "serviceId": SERVICE_ID},
            headers={"Authorization": f"Bearer {IMEI_CHECK_API_KEY}"},
            ssl=False
        ) as response:
            res = await response.json()
            if response.status != 201:
                raise IMEICheckError(res.get("mes sage"), response.status)
            properties = res.get("properties")
            if not properties:
                raise IMEICheckError("Информация не найдена", 404)
            return IMEICheckResponse(
                device_name=properties.get("deviceName"), 
                imei=properties.get("imei"),
                meid=properties.get("meid"),
                imei2=properties.get("imei2"),
                modelDesc=properties.get("modelDesc"),
            )