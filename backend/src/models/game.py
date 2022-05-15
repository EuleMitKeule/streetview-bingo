from __future__ import annotations
from common import *
from models import add_schema, User, GameWord, TokenModel

game_user_table = db.Table(
    'game_user', db.Model.metadata,
    db.Column('game_id', db.Integer, db.ForeignKey('game.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)


@add_schema(
    users=ma.Nested(User.Schema, many=True, exclude=["token"]),
    moderator=ma.Nested(User.Schema, exclude=["token"]),
    words=ma.Nested(GameWord.Schema, many=True)
)
class Game(TokenModel):
    __tablename__ = "game"
    status = db.Column(db.String(16), default="created")
    users = db.relationship("User", secondary=game_user_table)
    words = db.relationship("GameWord", backref="game", foreign_keys='GameWord.game_id')
    lobby_id = db.Column(db.Integer, db.ForeignKey("lobby.id"))

    moderator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    moderator = db.relationship("User", foreign_keys='Game.moderator_id')