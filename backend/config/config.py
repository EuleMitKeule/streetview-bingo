from os import path
from config.database_config import DatabaseConfig, SqliteConfig, MysqlConfig


basedir: str = path.abspath(path.dirname(__file__))


class Config:
    database_config: DatabaseConfig = SqliteConfig(path=path.join(basedir, "streetview-bingo.log"))
    log_path: str = path.join(basedir, "streetview-bingo.log")
