from pydantic import BaseModel


class IMEICheckModel(BaseModel):
    imei: str
    token: str


class IMEICheckResponse(BaseModel):
    device_name: str
    imei: str 
    meid: str = "Нет информации"
    imei2: str = "Нет информации"