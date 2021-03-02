from config import db, ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import Nested

class Word(db.Model):
    __tablename__ = "word"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), index=True)

class Lobby(db.Model):
    __tablename__ = "lobby"
    id = db.Column(db.Integer, primary_key=True)

    users = db.relationship("User", backref="lobby", foreign_keys='User.lobby_id')
    owner = db.relationship("User", backref="owned_lobby", uselist=False, foreign_keys='User.owned_lobby_id')

    token = db.Column(db.String(16), index=True)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    token = db.Column(db.String(16), index=True)

    lobby_id = db.Column(db.Integer, db.ForeignKey("lobby.id"))
    owned_lobby_id = db.Column(db.Integer, db.ForeignKey("lobby.id"))

class WordSchema(ModelSchema):
    class Meta:
        model = Word
        sqla_session = db.session

class UserSchema(ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session

class LobbySchema(ModelSchema):
    class Meta:
        model = Lobby
        sqla_session = db.session

    users = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby"], many=True)
    owner = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby"])
