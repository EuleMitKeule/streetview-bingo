from config import db, ma
from marshmallow_sqlalchemy import ModelSchema

class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), index=True)

class WordSchema(ModelSchema):
    class Meta:
        model = Word
        sqla_session = db.session

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    token = db.Column(db.String(16), index=True)

class UserSchema(ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session