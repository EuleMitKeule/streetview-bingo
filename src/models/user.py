from src.models import BaseModel, add_schema, add_view
from src.common import db


@add_view()
@add_schema()
class User(BaseModel):
    __tablename__ = "users"

    name: str = db.Column(db.String(255), nullable=False, default="")
    lobby_id: int = db.Column(db.Integer, db.ForeignKey("lobbies.id"))
    owned_lobby_id: int = db.Column(db.Integer, db.ForeignKey("lobbies.id"))
    moderated_lobby_id: int = db.Column(db.Integer, db.ForeignKey("lobbies.id"))
    ready: bool = db.Column(db.Boolean, default=False)
    color: str = db.Column(db.String(255), nullable=False, default="")