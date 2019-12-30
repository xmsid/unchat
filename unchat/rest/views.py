import aiohttp
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/")
async def test(request: aiohttp.web_request.Request):
    return web.json_response(data=dict(request.headers))
