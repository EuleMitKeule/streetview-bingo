from dataclasses import dataclass, field

from src.const import DEFAULT_SQLITE_PATH
from src.config.models import LoggingModel


@dataclass
class SqliteModel:
    path: str = field(default=DEFAULT_SQLITE_PATH, metadata=dict(required=False))
    recreate: bool = field(default=False, metadata=dict(required=False))
