from typing_extensions import Self
import yaml
from marshmallow_dataclass import class_schema
import logging
from os import path
import os
from dataclasses import dataclass, field


@dataclass
class ConfigModel:

    @dataclass
    class NetworkingConfig:
        port: int = 5000
        host: str = "localhost"

    @dataclass
    class SqliteConfig:
        db_path: str = field(metadata=dict(required=True))
        recreate: bool = False

    secret_key: str = field(metadata=dict(required=True))
    networking: NetworkingConfig = field(metadata=dict(required=False))
    sqlite: SqliteConfig = field(metadata=dict(required=True))


class Config:

    config_model: ConfigModel

    def __init__(self):
        pass

    def load(self, config_path: str):
        if not path.exists(config_path):
            config_path = os.path.join(os.getcwd(), config_path)

        if not path.exists(config_path):
            logging.error(f"Config file does not exist at path {config_path}")
            logging.error(f"Current working directory: {os.getcwd()}")
            exit(1)

        with open(config_path, "r") as f:
            config_dict: dict = yaml.safe_load(f)

        config_schema = class_schema(ConfigModel)()
        self.config_model = config_schema.load(config_dict)



