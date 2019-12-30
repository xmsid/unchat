import logging
from app import App

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)-15s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M:%S",
)
logging.getLogger("aiohttp.access").setLevel(logging.ERROR)
app = App()
app.run()
