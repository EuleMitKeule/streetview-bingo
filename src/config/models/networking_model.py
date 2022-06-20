from dataclasses import field
from marshmallow_dataclass import dataclass

from src.const import DEFAULT_HOST, DEFAULT_PORT


@dataclass
class NetworkingModel:
    port: int = field(default=DEFAULT_PORT, metadata=dict(required=False))
    host: str = field(default=DEFAULT_HOST, metadata=dict(required=False))

