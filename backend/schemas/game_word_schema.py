from flask import current_app
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from models.game_word import GameWord
from schemas.user_schema import UserSchema

db = current_app.db


class GameWordSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GameWord
        sqla_session = db.session
        load_instance = True
        include_relationships = True

    users = Nested(UserSchema, exclude=["token", "lobby", "owned_lobby", "moderated_games"], many=True)
