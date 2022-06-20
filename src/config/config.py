from logging import NOTSET, FileHandler, Handler, Logger, RootLogger, StreamHandler, getLogger
import logging
from logging.handlers import RotatingFileHandler, MemoryHandler
import os
from typing import Optional, Type
from flask import Flask
from flask_marshmallow import Schema
from marshmallow import ValidationError
from marshmallow_dataclass import class_schema
from yaml import safe_dump, safe_load
from src.config.models import LoggingModel, LoggerModel

from src.const import (
    APP_NAME,
    APP_VERSION,
    DEFAULT_CONFIG_PATH
)
from src.config import ConfigModel


class Config:
    config_model: ConfigModel = ConfigModel()
    app: Optional[Flask] = None
    loggers: list[Logger] = []
    root_logger: Logger

    def __init__(self, app: Flask = None):        
        self.root_logger = getLogger("root")
        if app:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        self.app = app

        config_path: str = os.environ.get("CONFIG_PATH", DEFAULT_CONFIG_PATH)

        self.configure_pre_logging()

        logging.info(f"Starting {APP_NAME}...")
        logging.info(f"Loading config from {os.path.abspath(config_path)}.")

        if not os.path.exists(config_path):
            logging.warn(f"Config file does not exist at path {config_path}. Using default config.")
            self.create_default()
        else:
            with open(config_path, "r") as f:
                config_dict: dict = safe_load(f)

            config_schema = class_schema(ConfigModel)()

            try:
                self.config_model = config_schema.load(config_dict)
            except ValidationError as e:
                logging.error(f"Config file is invalid.")
                logging.error(e)
                exit(1)
            except Exception as e:
                logging.error(f"Failed to load config.")
                logging.error(e)
                exit(1)

        self.create_folders()
        self.configure_post_logging()

        logging.info(f"Using database file at {os.path.abspath(self.config_model.sqlite.path)}.")

        app.config["TESTING"] = self.config_model.testing
        app.config["DEBUG"] = self.config_model.debug and not self.config_model.testing
        app.config["SECRET_KEY"] = self.config_model.secret_key
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.abspath(self.config_model.sqlite.path)}"
        app.config["SCHEDULER_API_ENABLED"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["API_TITLE"] = APP_NAME
        app.config["API_VERSION"] = APP_VERSION
        app.config["OPENAPI_VERSION"] = "3.0.0"
        app.config["OPENAPI_URL_PREFIX"] = "/"
        app.config["OPENAPI_JSON_PATH"] = "openapi.json"
        app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui/"
        app.config["OPENAPI_SWAGGER_UI_URL"] = self.config_model.openapi.swagger_url
        app.config["OPENAPI_REDOC_PATH"] = "/redoc/"
        app.config["OPENAPI_REDOC_URL"] = self.config_model.openapi.redoc_url
        app.config["API_SPEC_OPTIONS"] = {
            "components": {
                "securitySchemes": {
                    "bearerAuth": {
                        "type": "http",
                        "scheme": "bearer",
                        "bearerFormat": "JWT",
                        "in": "header"
                    }
                }
            },
        }

    def create_folders(self):
        folders: list[str] = [
            os.path.dirname(os.path.abspath(self.config_model.sqlite.path))
        ]

        for logger in self.loggers:
            path: str = self.config_model.logging.get_path(logger.name)
            recreate: bool = self.config_model.logging.get_recreate(logger.name)
            if recreate:
                if os.path.exists(os.path.abspath(path)):
                    os.remove(path)

            folders.append(os.path.dirname(os.path.abspath(path)))

        for folder in folders:
            try:
                if not os.path.exists(folder):
                    os.makedirs(folder)
            except Exception as e:
                logging.error(f"Failed to create folder: {folder}")
                logging.error(e)
                exit(1)

    def create_default(self):
        logging.info(f"Creating default config file at {DEFAULT_CONFIG_PATH}.")

        self.config_model = ConfigModel()

        config_schema: Schema = class_schema(ConfigModel)()

        try:
            config_dict: dict = config_schema.dump(self.config_model)
            with open(DEFAULT_CONFIG_PATH, "w") as f:
                f.write(safe_dump(config_dict))
            logging.info("Default config file created.")
        except Exception as e:
            logging.error(f"Failed to create default config.")
            logging.error(e)
            exit(1)

    def configure_pre_logging(self):

        self.setup_loggers()

        self.disable_handlers()
        self.enable_handlers(StreamHandler)
        self.enable_handlers(MemoryHandler)

    def configure_post_logging(self):

        self.setup_loggers()

        self.enable_handlers(StreamHandler)
        self.enable_handlers(FileHandler)
        self.disable_handlers(MemoryHandler)

        logging.info(f"Using log file at {self.config_model.logging.path}.")

    def setup_loggers(self) -> None:
        self.root_logger.name = APP_NAME
        self.app.logger = self.root_logger

        loggers: list[Logger] = [
            self.root_logger,
            getLogger("werkzeug"),
            getLogger("sqlalchemy"),
            getLogger("apscheduler"),
            getLogger("passlib")
        ]

        for logger in loggers:
            if not logger in self.loggers:
                self.loggers.append(logger)
            logger.setLevel(self.config_model.logging.get_level(logger.name))
            logger.propagate = self.config_model.logging.get_propagate(logger.name)

    def configure_test_logging(self):
        if not self.app:
            return

        if not self.app.config.get("TESTING", False):
            return

        self.disable_handlers(StreamHandler)

    def enable_handlers(self, handler_type: Type[Handler]):
        self.disable_handlers(handler_type)

        for logger in self.loggers:

            if self.config_model.logging.get_disable(logger.name):
                continue

            if logger.parent == self.root_logger and logger.propagate:
                continue

            handler: Optional[Handler] = None
            
            match handler_type.__qualname__:
                case MemoryHandler.__qualname__:
                    handler = self.config_model.logging.get_memory_handler(logger.name)
                case FileHandler.__qualname__:
                    handler = self.config_model.logging.get_file_handler(logger.name)
                case _:
                    handler = handler_type()

            handler.setFormatter(self.config_model.logging.get_formatter(logger.name))
            handler.setLevel(self.config_model.logging.get_level(logger.name))
            logger.addHandler(handler)

    def disable_handlers(self, handler_type: Type[Handler] = None):
        if handler_type:
            for logger in self.loggers:
                handler: Handler = self.get_handler(logger, handler_type)
                
                if not handler:
                    continue

                match handler_type.__qualname__:
                    case MemoryHandler.__qualname__:
                        file_handler: Optional[FileHandler] = self.get_handler(logger, FileHandler) 
                        if file_handler:
                            handler.setTarget(file_handler)

                handler.close()
                logger.removeHandler(handler)
        else:
            for logger in self.loggers:
                for handler in logger.handlers:
                    handler.close()
                    logger.removeHandler(handler)

    def get_handler(self, logger: Logger, handler_type: Type[Handler]) -> Handler:
        for handler in logger.handlers:
            if isinstance(handler, handler_type):
                return handler

        return None
