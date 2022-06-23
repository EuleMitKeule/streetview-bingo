import random
import string
from src.models import BaseModel, add_schema, add_view, OperationType
from src.common import db, ma
from src.models import User, Word
from sqlalchemy.ext.hybrid import hybrid_property


@add_view()
@add_schema(
    meta={
        "exclude": [
            "_state",
            "_lobby_state",
        ]
    },
    users=ma.Nested(
        User.Schema, 
        many=True
    ),
    moderator=ma.Nested(
        User.Schema,
    ),
    owner=ma.Nested(
        User.Schema,
    ),
    words=ma.Nested(
        Word.Schema,
        many=True
    ),
    state=ma.String(
        attribute="_state"
    ),
    lobby_state=ma.String(
        attribute="_lobby_state"
    ),
)
class Lobby(BaseModel):
    __tablename__ = "lobbies"
    
    token: str = db.Column(db.String(64))

    _state: str = db.Column(
        db.String(16),
        default="lobby",
        nullable=False
    )

    _lobby_state: str = db.Column(
        db.String(16),
        default="moderator",
        nullable=False
    )

    owner: User = db.relationship("User", uselist=False, foreign_keys="User.owned_lobby_id")
    users: list[User] = db.relationship("User", uselist=True, foreign_keys="User.lobby_id")
    moderator: User = db.relationship("User", uselist=False, foreign_keys="User.moderated_lobby_id")
    
    words: list[Word] = db.relationship("Word", foreign_keys="Word.lobby_id")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = self.generate_token(8)

    @hybrid_property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if value == "finished":
            self.delete()
            return

        self._state = value

    @hybrid_property
    def lobby_state(self):
        return self._lobby_state

    @lobby_state.setter
    def lobby_state(self, value):
        self._lobby_state = value

    def add_user(self, user: User):
        self.users.append(user)
        self.save()

    @classmethod
    def generate_token(cls, length: int) -> str:
        letters = string.ascii_letters + string.digits
        token = ''.join(random.choice(letters) for _ in range(length))
        return token
