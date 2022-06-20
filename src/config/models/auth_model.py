from dataclasses import field
from marshmallow_dataclass import dataclass


@dataclass
class AuthModel:
    admin_username: str = field(default="admin", metadata=dict(required=False))
    admin_password: str = field(default="admin", metadata=dict(required=False))
