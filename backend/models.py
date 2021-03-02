from config import db, ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import Nested


game_user_table = db.Table('game_user', db.Model.metadata,
    db.Column('game_id', db.Integer, db.ForeignKey('game.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

word_user_table = db.Table('word_user', db.Model.metadata,
    db.Column('word_id', db.Integer, db.ForeignKey('game_word.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)


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
    moderated_games = db.relationship("Game", backref="moderator", foreign_keys='Game.moderator_id')


class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(16), index=True)
    status = db.Column(db.String(16))
    moderator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    users = db.relationship("User", secondary=game_user_table)
    words = db.relationship("GameWord", backref="game", foreign_keys='GameWord.game_id')


class GameWord(db.Model):
    __tablename__ = "game_word"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), index=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    users = db.relationship("User", secondary=word_user_table)


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


class GameSchema(ModelSchema):
    class Meta:
        model = Game
        sqla_session = db.session

    users = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby", "moderated_games"], many=True)
    moderator = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby", "moderated_games"])
    words = Nested(WordSchema, many=True) 


class GameWordSchema(ModelSchema):
    class Meta:
        model = GameWord
        sqla_session = db.session