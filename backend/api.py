from flask.json import jsonify

from schemas.word_schema import WordSchema
from schemas.user_schema import UserSchema
from schemas.lobby_schema import LobbySchema
from schemas.game_schema import GameSchema
import services.word_service as word_service
import services.lobby_service as lobby_service
import services.user_service as user_service
import services.game_service as game_service
import services.game_word_service as game_word_service


def create_lobby(body):

    owner_name = body['username']

    user = user_service.create_user(name=owner_name)
    lobby = lobby_service.create_lobby(owner=user)

    user_schema = UserSchema()
    user_result = user_schema.dump(user)

    lobby_schema = LobbySchema()
    lobby_result = lobby_schema.dump(lobby)

    result = {
        "user": user_result,
        "lobby": lobby_result
    }

    return result


def get_lobby(lobby_token, user_token):

    lobby = lobby_service.get_lobby(lobby_token=lobby_token)

    lobby_schema = LobbySchema()
    result = jsonify(lobby_schema.dump(lobby))

    return result


def join_lobby(lobby_token, body):

    name = body['username']
    user = user_service.create_user(name=name)

    lobby_service.join_lobby(user=user, lobby_token=lobby_token)

    user_schema = UserSchema()
    result = jsonify(user_schema.dump(user))

    return result


def create_game(lobby_token, body):

    moderator_id = body['moderator']['id']

    game = game_service.create_game(lobby_token=lobby_token, moderator_id=moderator_id)

    game_schema = GameSchema()
    result = jsonify(game_schema.dump(game))

    return result


def get_game(lobby_token, game_token):

    game = game_service.get_game(game_token=game_token)

    game_schema = GameSchema()
    result = jsonify(game_schema.dump(game))

    return result


def update_game(lobby_token, game_token, user_token, body):

    if not game_service.is_moderator(game_token=game_token, user_token=user_token):
        return {"message": "You are not moderator"}, 403

    status = body['status']

    word_texts = []
    for word in body['words']:
        word_texts.append(word["text"])

    game = game_service.update_game(game_token=game_token, user_token=user_token, status=status, texts=word_texts)

    game_schema = GameSchema()
    result = jsonify(game_schema.dump(game))

    print(result.get_data(as_text=True))

    return result


def create_word_status(lobby_token, game_token, user_token, word_id, user_id):

    successful = game_word_service.set_found(
        game_token=game_token,
        user_token=user_token,
        game_word_id=word_id,
        user_id=user_id
    )

    if not successful:
        return {"message": "You are not moderator"}, 403

    return {"message": "OK"}, 200


def delete_word_status(lobby_token, game_token, user_token, word_id, user_id):

    successful = game_word_service.set_not_found(
        game_token=game_token,
        user_token=user_token, game_word_id=word_id,
        user_id=user_id
    )

    if not successful:
        return {"message": "You are not moderator"}, 403

    return {"message": "OK"}, 200


def get_user(user_token):

    user = user_service.get_user(user_token=user_token)
    user_schema = UserSchema()
    result = jsonify(user_schema.dump(user))

    return result


def get_words(length):

    words = word_service.get_random_words(length)
    word_schema = WordSchema(many=True)
    result = jsonify(word_schema.dump(words))

    return result
