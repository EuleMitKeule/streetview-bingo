from models import add_schema, BaseModel, User
from common import *


word_user_table = db.Table(
    'word_user', db.Model.metadata,
    db.Column('word_id', db.Integer, db.ForeignKey('game_word.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)


@add_schema(
    users=ma.Nested(User.Schema, many=True, exclude=["token"])
)
class GameWord(BaseModel):
    __tablename__ = "game_word"
    text: str = db.Column(db.String(32), index=True)
    game_id: int = db.Column(db.Integer, db.ForeignKey("game.id"))
    users: list = db.relationship("User", secondary=word_user_table)