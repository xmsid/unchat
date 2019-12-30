import aiohttp
from aiohttp import web
import logging
from .views import routes


class RestServer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.app = web.Application(middlewares=[self.logging_middleware])
        self.register_routes()

    @web.middleware
    async def logging_middleware(self, request: aiohttp.web_request.Request, handler):
        response: aiohttp.web_response.Response = await handler(request)
        self.logger.info(
            f"{request.remote} -> {request.path} {response.status} {response.reason} {request.headers.get('user-agent')}"
        )
        return response

    def register_routes(self):
        self.app.add_routes(routes)

    async def start(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, "localhost", 8080)  # TODO: make ip/port configurable
        await site.start()
