from flask import current_app
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.user import User

db = current_app.db


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
        include_relationships = True
