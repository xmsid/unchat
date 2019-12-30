import asyncio
from rest import RestServer


class App:
    def __init__(self):
        self.rest = RestServer()

    def run(self):
        asyncio.run(self.start())

    async def start(self):
        await self.rest.start()
        await asyncio.sleep(999999)
        # ^ This'll change i swear, I'm just using it rn to keep the process from exiting
