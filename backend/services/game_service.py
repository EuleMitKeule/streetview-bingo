from typing import List
from config import db
from models import Game, GameWord
import services.token_service as token_service
import services.user_service as user_service
import services.lobby_service as lobby_service


def get_game(game_id: int = None, game_token: str = None):
    """
    Returns a game from the game database.

    :param game_id: The ID of the game to return.
    :param game_token: The token of the game to return.
    :return: The game if found.
    """
    if game_id is not None:
        return Game.query.filter(Game.id == game_id).first()
    elif game_token is not None:
        return Game.query.filter(Game.token == game_token).first()
    else:
        return None


def create_game(lobby_token: str, moderator_id: int):
    """
    Creates a new game.

    :param lobby_token: The token of the lobby the game belongs to.
    :param moderator_id: The ID of the user that moderates the game.
    :return: The created game if successful.
    """
    token = token_service.generate_token(16)
    moderator = user_service.get_user(moderator_id)
    game = Game(token=token, status="created", moderator=moderator)

    lobby = lobby_service.get_lobby(lobby_token=lobby_token)
    game.users = lobby.users
    lobby.games.append(game)

    db.session.add(game)

    db.session.commit()
    return game


def delete_game(game_token: str):
    """
    Deletes a game from the game database.

    :param game_token: The token of the game to delete.
    """
    game = get_game(game_token=game_token)
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
    game = get_game(game_token=game_token)

    if game.moderator.token != user_token:
        return None

    if status is not None:
        game.status = status

    game_words = []

    if texts is not None:
        for text in texts:
            game_word = GameWord(text=text, game_id=game.id)
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
    game = get_game(game_token=game_token)

    return game.moderator.token == user_token
