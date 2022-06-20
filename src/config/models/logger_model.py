from dataclasses import field
from importlib import import_module
from logging import NOTSET, FileHandler, Formatter, StreamHandler
import logging
from logging.handlers import MemoryHandler, RotatingFileHandler
from marshmallow_dataclass import dataclass

from src.const import (
    DEFAULT_DATE_FORMAT,
    DEFAULT_LOG_FORMAT, 
    DEFAULT_LOG_LEVEL,
    DEFAULT_LOG_MAX_FILES,
    DEFAULT_LOG_MAX_SIZE, 
    DEFAULT_LOG_PATH,
    DEFAULT_LOG_PROPAGATE,
    DEFAULT_LOG_STREAM,
)


@dataclass
class LoggerModel:
    name: str = field(metadata=dict(required=True))
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

    def get_formatter(self, **kwargs):
        return Formatter(
            fmt=self.format if self.format else kwargs.get("fmt", DEFAULT_LOG_FORMAT),
            datefmt=self.date_format if self.date_format else kwargs.get("datefmt", DEFAULT_DATE_FORMAT)
        )

    def get_stream_handler(self, **kwargs):
        try:
            return StreamHandler(
                stream=import_module(self.stream) if self.stream else kwargs.get("stream", DEFAULT_LOG_STREAM)
            )
        except ModuleNotFoundError as e:
            logging.error(f"Stream handler {self.stream} not found")
            logging.error(e)
            exit(1)

    def get_file_handler(self, **kwargs):
        return RotatingFileHandler(
            filename=self.path if self.path else kwargs.get("filename", DEFAULT_LOG_PATH),
            mode="a",
            encoding="utf-8",
            maxBytes=self.max_size if self.max_size else kwargs.get("maxBytes", DEFAULT_LOG_MAX_SIZE),
            backupCount=self.max_files if self.max_files else kwargs.get("backupCount", DEFAULT_LOG_MAX_FILES)
        ) if self.rotate else FileHandler(
            filename=self.path if self.path else kwargs.get("filename", DEFAULT_LOG_PATH),
            mode="a",
            encoding="utf-8",
            delay=False
        )

    def get_memory_handler(self):
        return MemoryHandler(capacity=100, flushLevel=NOTSET)
    