from dataclasses import field
from importlib import import_module
from logging import NOTSET, FileHandler, Formatter, StreamHandler
import logging
from logging.handlers import MemoryHandler, RotatingFileHandler
from typing import Optional
from marshmallow_dataclass import dataclass

from src.const import (
    APP_NAME,
    DEFAULT_DATE_FORMAT,
    DEFAULT_LOG_FORMAT, 
    DEFAULT_LOG_LEVEL,
    DEFAULT_LOG_MAX_FILES,
    DEFAULT_LOG_MAX_SIZE, 
    DEFAULT_LOG_PATH,
    DEFAULT_LOG_PROPAGATE,
    DEFAULT_LOG_STREAM,
)
from src.config.models import LoggerModel


@dataclass
class LoggingModel:
    disable: bool = field(default=False, metadata=dict(required=False))
    recreate: bool = field(default=False, metadata=dict(required=False))
    level: str = field(default=DEFAULT_LOG_LEVEL, metadata=dict(required=False))
    format: str = field(default=DEFAULT_LOG_FORMAT, metadata=dict(required=False))
    date_format: str = field(default=DEFAULT_DATE_FORMAT, metadata=dict(required=False))
    path: str = field(default=DEFAULT_LOG_PATH, metadata=dict(required=False))
    rotate: bool = field(default=True, metadata=dict(required=False))
    max_size: int = field(default=DEFAULT_LOG_MAX_SIZE, metadata=dict(required=False))
    max_files: int = field(default=DEFAULT_LOG_MAX_FILES, metadata=dict(required=False))
    stream: str = field(default=DEFAULT_LOG_STREAM, metadata=dict(required=False))
    propagate: bool = field(default=DEFAULT_LOG_PROPAGATE, metadata=dict(required=False))
    loggers: list[LoggerModel] = field(default_factory=list, metadata=dict(required=False))

    def get_disable(self, logger_name: str):
        logger_model = self._get_logger_model(logger_name)
        return logger_model.disable if logger_model else self.disable
    
    def get_level(self, logger_name: str):
        logger_model = self._get_logger_model(logger_name)
        return logger_model.level if logger_model else self.level

    def get_path(self, logger_name: str):
        logger_model: LoggerModel = self._get_logger_model(logger_name)
        return logger_model.path if logger_model else self.path

    def get_recreate(self, logger_name: str):
        logger_model = self._get_logger_model(logger_name)
        return logger_model.recreate if logger_model else self.recreate

    def get_propagate(self, logger_name: str):
        logger_model = self._get_logger_model(logger_name)
        return logger_model.propagate if logger_model else self.propagate

    def get_formatter(self, logger_name: Optional[str] = None):
        if logger_name:
            logger_model: LoggerModel = self._get_logger_model(logger_name)
            if logger_model:
                return logger_model.get_formatter(fmt=self.format, datefmt=self.date_format)
        return Formatter(
            fmt=self.format,
            datefmt=self.date_format
        )

    def get_stream_handler(self, logger_name: Optional[str] = None):
        if logger_name:
            logger_model: LoggerModel = self._get_logger_model(logger_name)
            if logger_model:
                return logger_model.get_stream_handler(stream=self.stream)
        try:
            stream = import_module(self.stream)
            return StreamHandler(
                stream=stream
            )
        except ModuleNotFoundError as e:
            logging.error(f"Stream handler {self.stream} not found")
            logging.error(e)
            exit(1)

    def get_file_handler(self, logger_name: Optional[str] = None):
        if logger_name:
            logger_model: LoggerModel = self._get_logger_model(logger_name)
            if logger_model:
                return logger_model.get_file_handler(
                    filename=self.path, 
                    max_size=self.max_size, 
                    max_files=self.max_files, 
                    rotate=self.rotate
                )
        return RotatingFileHandler(
            filename=self.path,
            mode="a",
            encoding="utf-8",
            maxBytes=self.max_size,
            backupCount=self.max_files
        ) if self.rotate else FileHandler(
            filename=self.path,
            mode="a",
            encoding="utf-8",
            delay=False
        )

    def get_memory_handler(self, logger_name: Optional[str] = None):
        if logger_name:
            logger_model: LoggerModel = self._get_logger_model(logger_name)
            if logger_model:
                return logger_model.get_memory_handler()
        return MemoryHandler(capacity=100, flushLevel=NOTSET)

    def _get_logger_model(self, logger_name: str) -> Optional[LoggerModel]:
        for logger_model in self.loggers:
            if logger_model.name == logger_name:
                return logger_model
        return None
