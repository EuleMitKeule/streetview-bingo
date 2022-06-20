from dataclasses import field
from marshmallow_dataclass import dataclass

from src.const import DEFAULT_SECRET_KEY
from src.config.models import *


@dataclass
class ConfigModel:

    secret_key: str = field(default=DEFAULT_SECRET_KEY, metadata=dict(required=False))
    debug: bool = field(default=False, metadata=dict(required=False))
    testing: bool = field(default=False, metadata=dict(required=False))
    logging: LoggingModel = field(default=LoggingModel(), metadata=dict(required=False))
    sqlite: SqliteModel = field(default=SqliteModel(), metadata=dict(required=False))
    networking: NetworkingModel = field(default=NetworkingModel(), metadata=dict(required=False))
    auth: AuthModel = field(default=AuthModel(), metadata=dict(required=False))
    openapi: OpenApiModel = field(default=OpenApiModel(), metadata=dict(required=False))
    apscheduler: ApSchedulerModel = field(default=ApSchedulerModel(), metadata=dict(required=False))
