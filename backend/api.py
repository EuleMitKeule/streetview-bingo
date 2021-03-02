from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
import connexion
from sqlalchemy.sql.expression import func
from config import connex_app, db
from models import Word, WordSchema, User, UserSchema, Lobby, LobbySchema, Game, GameSchema
from marshmallow import ValidationError
import string
import random
import services.word_service as word_service
import services.lobby_service as lobby_service
import services.user_service as user_service
import services.token_service as token_service
import services.game_service as game_service


def create_lobby(body):
    
    name = body['username']

    user = user_service.create_user(name=name)
    lobby = lobby_service.create_lobby(owner=user)

    user_schema = UserSchema()
    user_result = jsonify(user_schema.dump(user))

    lobby_schema = LobbySchema()
    lobby_result = jsonify(lobby_schema.dump(lobby))
    
    result = {
        "user": user_result,
        "lobby": lobby_result
    }

    return result

def get_lobby(lobby_token, user_token):

    lobby = lobby_service.get_lobby(lobby_token)

    lobby_schema = LobbySchema()
    result = jsonify(lobby_schema.dump(lobby))

    return result


def join_lobby(lobby_token, body):

    name = body['username']
    user = user_service.create_user(name)

    lobby_service.join_lobby(user, lobby_token)

    user_schema = UserSchema()
    result = jsonify(user_schema.dump(user))

    return result

def create_game(body):

    moderator_id = body['moderator']['id']

    game = game_service.create_game(moderator_id)

    game_schema = GameSchema()
    result = jsonify(game_schema.dump(game))

    return result

def update_game(lobby_token, game_token, user_token, body):

    game = game_service.update_game(lobby_token, game_token, user_token, body)

    if game is None:
        return {"message": "You are not moderator"}, 403

    game_schema = GameSchema()
    result = jsonify(game_schema.dump(game))

    print(result.get_data(as_text=True))

    return result


def create_word_status():
    pass


def delete_word_status():
    pass


def get_words(length):

    words = word_service.get_random_words(length)
    word_schema = WordSchema(many=True)
    result = jsonify(word_schema.dump(words))

    return result


if __name__ == "__main__":
    CORS(connex_app.app)
    connex_app.add_api('openapi.yaml', strict_validation=True, validate_responses=True, base_path="/api")
    connex_app.add_api('angular.yaml', options={"swagger_ui": False})
    connex_app.run()