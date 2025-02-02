from aiohttp import ClientSession
from api.requests.imei_requests import IMEIRequests


class APIRequests:
    def __init__(self, session: ClientSession):
        self.imei_requests = IMEIRequests(session=session)