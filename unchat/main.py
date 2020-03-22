import logging
from app import Unchat

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)-15s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M:%S",
)
logging.getLogger("aiohttp.access").setLevel(logging.ERROR)
unchat = Unchat()
unchat.run(host="localhost", port=3000)
