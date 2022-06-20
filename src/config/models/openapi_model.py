from dataclasses import field
from marshmallow_dataclass import dataclass

from src.const import DEFAULT_REDOC_URL, DEFAULT_SWAGGER_UI_URL


@dataclass
class OpenApiModel:

    swagger_url: str = field(default=DEFAULT_SWAGGER_UI_URL, metadata=dict(required=False))
    redoc_url: str = field(default=DEFAULT_REDOC_URL, metadata=dict(required=False))
