from config import db, ma
from marshmallow_sqlalchemy import ModelSchema

class Word(db.Model):
    __tablename__ = "words"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), index=True)

#a lobby contains multiple users, a user is child of one lobby
#running python ./backend/build_database.py gives sqlalchemy.exc.AmbiguousForeignKeysError

class Lobby(db.Model):
    __tablename__ = "lobbies"
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship("User", backref="lobby") #One-To-Many relationship
    owner = db.Column(db.Integer, db.ForeignKey("users.id"))
    token = db.Column(db.String(16), index=True)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    token = db.Column(db.String(16), index=True)
    lobby_id = db.Column(db.Integer, db.ForeignKey("lobbies.id")) #backref foreign key column
    
class WordSchema(ModelSchema):
    class Meta:
        model = Word
        sqla_session = db.session

class LobbySchema(ModelSchema):
    class Meta:
        model = Lobby
        sqla_session = db.session

class UserSchema(ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session
