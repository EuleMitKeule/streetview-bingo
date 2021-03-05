from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from models import Word, User, GameWord, Game, Lobby
from flask import current_app


db = current_app.db


class WordSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Word
        sqla_session = db.session
        load_instance = True
        include_relationships = True


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
        include_relationships = True


class GameWordSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GameWord
        sqla_session = db.session
        load_instance = True
        include_relationships = True

    users = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby", "moderated_games"], many=True)


class GameSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        sqla_session = db.session
        load_instance = True
        include_relationships = True

    users = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby", "moderated_games"], many=True)
    moderator = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby", "moderated_games"])
    words = Nested(GameWordSchema, many=True)


class LobbySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Lobby
        sqla_session = db.session
        load_instance = True
        include_relationships = True

    users = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby"], many=True)
    owner = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby"])
    games = Nested(GameSchema, many=True)