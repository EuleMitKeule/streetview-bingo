from flask import Blueprint, request, jsonify
from sqlalchemy import func

from common import *
from models import *


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/lobby/", methods=["POST"])
def create_lobby():
    body: dict = request.get_json()

    username: str = body.get("username")
    user: User = User.create(name=username)
    lobby: Lobby = Lobby.create(owner=user, users=[user])

    user_result = User.dump(user)
    lobby_result = Lobby.dump(lobby)

    result = {
        "user": user_result,
        "lobby": lobby_result
    }

    return jsonify(result)


@bp.route("/lobby/<lobby_token>", methods=["GET"])
def get_lobby(lobby_token: str):

    lobby: Lobby = Lobby.find_by_token(lobby_token)

    lobby_dict: dict = Lobby.dump(lobby)

    return jsonify(lobby_dict)


@bp.route("/lobby/<lobby_token>/join", methods=["POST"])
def join_lobby(lobby_token: str):
    body: dict = request.get_json()
    
    username: str = body.get("username")
    user: User = User.create(name=username)
    lobby: Lobby = Lobby.find_by_token(lobby_token)

    if user not in lobby.users:
        lobby.users.append(user)

    db.session.commit()
    sio.emit("reload", to=lobby_token)

    user_dict = User.dump(user)

    return jsonify(user_dict)


@bp.route("/lobby/<lobby_token>/rejoin, methods=['POST']")
def rejoin_lobby(lobby_token: str):    
    user_token: str = request.args.get("user_token")
    user: User = User.find_by_token(user_token)
    lobby: Lobby = Lobby.find_by_token(lobby_token)

    if user not in lobby.users:
        lobby.users.append(user)
        db.session.commit()
        sio.emit("reload", to=lobby_token)

    lobby_dict = Lobby.dump(lobby)

    return jsonify(lobby_dict)


@bp.route("/lobby/<lobby_token>/game/", methods=["POST"])
def create_game(lobby_token: str):
    body: dict = request.get_json()

    moderator_id: int = body['moderator']['id']

    moderator: User = User.find(moderator_id)
    lobby: Lobby = Lobby.find_by_token(lobby_token)
    game: Game = Game.create(moderator=moderator, users=lobby.users)
    lobby.add_game(game)

    db.session.commit()
    sio.emit("reload", to=lobby_token)

    game_dict = Game.dump(game)

    return jsonify(game_dict)


@bp.route("/lobby/<lobby_token>/game/<game_token>", methods=["GET"])
def get_game(lobby_token: str, game_token: str):

    game: Game = Game.find_by_token(game_token)
    game_dict: dict = Game.dump(game)

    return jsonify(game_dict)


@bp.route("/lobby/<lobby_token>/game/<game_token>", methods=["PUT"])
def update_game(lobby_token: str, game_token: str):
    body: dict = request.get_json()
    user_token: str = request.args.get("user_token")
    user: User = User.find_by_token(user_token)
    game: Game = Game.find_by_token(game_token)

    if user.token != game.moderator.token:
        return {"message": "You are not moderator"}, 403
        
    game: Game = Game.load(data=body)
    db.session.commit()

    sio.emit("reload", to=lobby_token)

    game_dict: dict = Game.dump(game)

    return jsonify(game_dict)


@bp.route("/lobby/<lobby_token>/game/<game_token>/words/<word_id>/users/<user_id>", methods=["POST"])
def create_word_status(lobby_token, game_token, word_id, user_id):
    game_word: GameWord = GameWord.find(word_id)
    user: User = User.find(user_id)

    user_token: str = request.args.get("user_token")
    game: Game = Game.find_by_token(game_token)

    if user_token != game.moderator.token:
        return {"message": "You are not moderator"}, 403

    if user not in game_word.users:
        game_word.users.append(user)

    db.session.commit()

    sio.emit("reload", to=lobby_token)

    return {"message": "OK"}, 200


@bp.route("/lobby/<lobby_token>/game/<game_token>/words/<word_id>/users/<user_id>", methods=["DELETE"])
def delete_word_status(lobby_token, game_token, word_id, user_id):
    game_word: GameWord = GameWord.find(word_id)
    user: User = User.find(user_id)

    user_token: str = request.args.get("user_token")
    game: Game = Game.find_by_token(game_token)

    if user_token != game.moderator.token:
        return {"message": "You are not moderator"}, 403

    if user in game_word.users:
        game_word.users.remove(user)
        
    db.session.commit()

    sio.emit("reload", to=lobby_token)

    return {"message": "OK"}, 200


@bp.route("/users", methods=["GET"])
def get_user():
    user_token: str = request.args.get("user_token")
    user: User = User.find_by_token(user_token)

    user_dict = User.dump(user)
    return jsonify(user_dict)


@bp.route("/word", methods=["POST"])
def create_word():
    body: dict = request.get_json()
    word: Word = Word.load(body)
        
    db.session.commit()

    word_dict = Word.dump(word)
    return jsonify(word_dict)


@bp.route("/word", methods=["GET"])
def get_words():
    length: int = request.args.get("length")
    words = Word.query.order_by(func.random()).limit(length).all()
    words_dict = Word.dump(words, many=True)

    return jsonify(words_dict)
