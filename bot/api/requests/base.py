from aiohttp import ClientSession


class BaseRequests:
    def __init__(self, session: ClientSession):
        self.session = session