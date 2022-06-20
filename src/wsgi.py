from src.common import sio
from src.config.config import config

sio.run(
    host=config.config_model.networking.host,
    port=config.config_model.networking.port
)
