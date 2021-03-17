from flask import current_app
from models.game import Game
from models.game_word import GameWord
from models.user import User
import services.game_service as game_service
import services.user_service as user_service


db = current_app.db


def get_game_word(game_word_id: int):
    """
    Returns a game word from the game word database

    :param game_word_id: The ID of the game word
    :return: The game word if found
    """
    game_word = GameWord.query.filter(GameWord.id == game_word_id).first()
    return game_word


def get_game_word_by_content(text: str, game_id: int = None, game_token: str = None):
    """
    Returns a game word from the game word database

    :param text: The text of the word to get
    :param game_id: The ID of the game the game word belongs to
    :param game_token: The token of the game the word belongs to
    :return: The game word if found
    """
    if game_id is not None:
        return GameWord.query\
            .filter(GameWord.text == text)\
            .filter(GameWord.game_id == game_id)\
            .first()
    elif game_token is not None:
        game = game_service.get_game(game_token=game_token)
        return GameWord.query\
            .filter(GameWord.text == text)\
            .filter(GameWord.game_id == game.id)\
            .first()
    else:
        return None


def create_game_word(text: str, game_token: str):
    """
    Creates a new game word.

    :param text: The text of the game word to create
    :param game_token: The token of the game the word belongs to
    :return: The created game word
    """
    game = game_service.get_game(game_token=game_token)
    game_word: GameWord = get_game_word_by_content(text, game_token=game_token)

    if game_word is None:
        game_word = GameWord(text=text)
        db.session.add(game_word)
        game.words.append(game_word)

    db.session.commit()
    return game_word


def delete_word(game_token: str, text: str):
    """
    Deletes a game word

    :param game_token: The token of the game the word belongs to
    :param text: The text of the game word to create
    """
    game = Game.query.filter(Game.token == game_token).first()

    GameWord.query\
        .filter(GameWord.game_id == game.id)\
        .filter(GameWord.text == text)\
        .delete()

    db.session.commit()


def set_found(game_token, user_token, game_word_id, user_id):
    """
    Sets the game word as found for specified user.

    :param game_token: The token of the game the word belongs to
    :param user_token: The token of the user performing the action
    :param game_word_id: The ID of the word to set as found
    :param user_id: The ID of the user to set as found for
    :return: True if successful, False if unathorized
    """
    game = Game.query.filter(Game.token == game_token).first()

    if game.moderator.token != user_token:
        return False

    game_word = GameWord.query.filter(GameWord.id == game_word_id).first()
    user = User.query.filter(User.id == user_id).first()

    game_word.users.append(user)

    db.session.commit()
    return True


def set_not_found(game_token, user_token, game_word_id, user_id):
    """
    Sets the word as not found for specified user.

    :param game_token: The token of the game the word belongs to
    :param user_token: The token of the user performing the action
    :param game_word_id: The ID of the word to set as not found
    :param user_id: The ID of the user to set as not found for
    :return: True if successful, False if unauthorized
    """
    if not game_service.is_moderator(game_token, user_token):
        return False

    game_word = get_game_word(game_word_id)
    user = user_service.get_user(user_id)

    game_word.users.remove(user)

    db.session.commit()
    return True
