from flask import current_app
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from models.game import Game
from schemas.game_word_schema import GameWordSchema
from schemas.user_schema import UserSchema

db = current_app.db


class GameSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        sqla_session = db.session
        load_instance = True
        include_relationships = True

    users = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby", "moderated_games"], many=True)
    moderator = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby", "moderated_games"])
    words = Nested(GameWordSchema, many=True)
