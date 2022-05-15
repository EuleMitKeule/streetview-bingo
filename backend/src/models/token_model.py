from __future__ import annotations
import random
import string

from common import db
from models import BaseModel


class TokenModel(BaseModel):
    __abstract__ = True

    token: str = db.Column(db.String(16), index=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token = self.generate_token(16)

    @classmethod
    def find_by_token(cls, token: str) -> BaseModel:
        return cls.query.filter_by(token=token).first()

    @classmethod
    def generate_token(cls, length: int) -> str:
        letters = string.ascii_letters + string.digits
        token = ''.join(random.choice(letters) for _ in range(length))
        return token
