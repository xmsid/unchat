import aiohttp
from aiohttp import web
from routes import routes


class Unchat(web.Application):
    def __init__(self):
        super().__init__(middlewares=[self.logging_middleware])
        self.register_routes()

    def run(self, *args, **kwargs):
        web.run_app(self, *args, **kwargs)

    @web.middleware
    async def logging_middleware(self, request: aiohttp.web_request.Request, handler):
        response: aiohttp.web_response.Response = await handler(request)
        self.logger.info(
            f"{request.remote} -> {request.path} {response.status} {response.reason} {request.headers.get('user-agent')}"
        )
        return response

    def register_routes(self):
        self.add_routes(routes)
