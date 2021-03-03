from typing import List
from config import db
from models import Game, GameWord
import services.token_service as token_service
import services.user_service as user_service
import services.lobby_service as lobby_service


def get_game_by_id(game_id: int):
    """
    Returns a game from the game database.

    :param game_id: The ID of the game to return.
    :return: The game if found.
    """
    game = Game.query.filter(Game.id == game_id).first()

    return game


def get_game_by_token(game_token: str):
    """
    Returns a game from the game database.

    :param game_token: The token of the game to return.
    :return: The game if found.
    """
    game = Game.query.filter(Game.token == game_token).first()

    return game


def create_game(lobby_token: str, moderator_id: int):
    """
    Creates a new game.

    :param lobby_token: The token of the lobby the game belongs to.
    :param moderator_id: The ID of the user that moderates the game.
    :return: The created game if successful.
    """
    token = token_service.generate_token(16)
    moderator = user_service.get_user_by_id(moderator_id)
    game = Game(token=token, status="created", moderator=moderator)

    lobby = lobby_service.get_lobby_by_token(lobby_token)
    game.users = lobby.users

    db.session.add(game)

    db.session.commit()
    return game


def delete_game(game_token: str):
    """
    Deletes a game from the game database.

    :param game_token: The token of the game to delete.
    """
    game = get_game_by_token(game_token)
    game.delete()

    db.session.commit()


def update_game(game_token: str, user_token: str, status: str = None, texts: List[str] = None):
    """
    Updates a games information.

    :param game_token: The token of the game to update.
    :param user_token: The token of the user that performs the action.
    :param status: (optional) Game status message to set.
    :param texts: (optional) List of word texts the game should contain.
    :return: The updated game if successful.
    """
    game = get_game_by_token(game_token)

    if game.moderator.token != user_token:
        return None

    if status is not None:
        game.status = status

    game_words = []

    if texts is not None:
        for text in texts:
            game_word = GameWord(text=text)
            db.session.add(game_word)
            game_words.append(game_word)

    game.words = game_words

    db.session.commit()
    return game


def is_moderator(game_token: str, user_token: str):
    """
    Checks if a user is the moderator of a game.

    :param game_token: The token of the game to check.
    :param user_token: The token of the user to check.
    :return: Whether the user is the moderator of the game.
    """
    game = get_game_by_token(game_token)

    return game.moderator.token == user_token
