from common import *
from models import add_schema, TokenModel


@add_schema(
)
class User(TokenModel):
    __tablename__ = "user"
    name = db.Column(db.String(32), index=True)
    lobby_id = db.Column(db.Integer, db.ForeignKey("lobby.id"))
    owned_lobby_id = db.Column(db.Integer, db.ForeignKey("lobby.id"))