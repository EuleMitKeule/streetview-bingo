from flask import current_app
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models.word import Word

db = current_app.db


class WordSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Word
        sqla_session = db.session
        load_instance = True
        include_relationships = True
