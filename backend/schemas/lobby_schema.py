from flask import current_app
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from models.lobby import Lobby
from schemas.game_schema import GameSchema
from schemas.user_schema import UserSchema

db = current_app.db


class LobbySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Lobby
        sqla_session = db.session
        load_instance = True
        include_relationships = True

    users = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby"], many=True)
    owner = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby"])
    games = Nested(GameSchema, many=True)
