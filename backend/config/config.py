from os import path
from config.database_config import DatabaseConfig, SqliteConfig, MysqlConfig
from config.networking_config import NetworkingConfig


basedir: str = path.abspath(path.dirname(__file__))


class Config:
    database_config: DatabaseConfig = SqliteConfig(path=path.join(basedir, "streetview-bingo.log"))
    networking_config: NetworkingConfig = NetworkingConfig(host="0.0.0.0", port=5000)
    log_path: str = path.join(basedir, "streetview-bingo.log")
