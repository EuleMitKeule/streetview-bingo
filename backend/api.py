from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
import connexion
from sqlalchemy.sql.expression import func
from config import connex_app, db
from models import Word, WordSchema, User, UserSchema, Lobby, LobbySchema
from marshmallow import ValidationError
import string
import random


def create_lobby(body):
    
    name = body['username']
    token = generate_token(16)

    #create new user
    user = User(name=name, token=token)
    db.session.add(user)
    
    #create new lobby
    token = generate_token(16)
    lobby = Lobby(owner=user, token=token)
    lobby.users.append(user)

    db.session.commit()

    lobby_schema = LobbySchema(many=False)
    result = jsonify(lobby_schema.dump(lobby))
    
    return result

def get_lobby(lobby_token, user_token):
    lobby = Lobby.query.filter(Lobby.token==lobby_token).first()
    lobby_schema = LobbySchema()
    result = jsonify(lobby_schema.dump(lobby))

    return result


def join_lobby():
    pass


def create_game():
    pass


def update_game():
    pass


def create_word_status():
    pass


def delete_word_status():
    pass


def get_words(length):

    words = Word.query.order_by(func.random()).limit(length).all()
    word_schema = WordSchema(many=True)
    result = jsonify(word_schema.dump(words))

    return result


def generate_token(length):
    letters = string.ascii_letters + string.digits
    token = ''.join(random.choice(letters) for i in range(length))
    return token

if __name__ == "__main__":
    CORS(connex_app.app)
    connex_app.add_api('openapi.yaml', strict_validation=True, validate_responses=True, base_path="/api")
    connex_app.add_api('angular.yaml', options={"swagger_ui": False})
    connex_app.run()