from config import db
from models import Game, User, GameWord
import game_service


def set_word_found(game_token, user_token, word_id, user_id):
    """
        Sets the word as found for specified user.

        :param game_token: The token of the game the word belongs to
        :param user_token: The token of the user performing the action
        :param word_id: The ID of the word to set as found
        :param user_id: The ID of the user to set as found for
        :return: True if successful, False if unathorized
    """
    game = Game.query.filter(Game.token == game_token).first()

    if game.moderator.token != user_token:
        return False

    game_word = GameWord.query.filter(GameWord.id == word_id).first()
    user = User.query.filter(User.id == user_id).first()

    game_word.users.append(user)

    db.session.commit()

    return True


def set_word_not_found(game_token, user_token, word_id, user_id):
    """
        Sets the word as not found for specified user.

        :param game_token: The token of the game the word belongs to
        :param user_token: The token of the user performing the action
        :param word_id: The ID of the word to set as not found
        :param user_id: The ID of the user to set as not found for
        :return: True if successful, False if unathorized
    """
    game = game_service.get_game(game_token)

    if game.moderator.token != user_token:
        return False

    game_word = GameWord.query.filter(GameWord.id == word_id).first()
    user = User.query.filter(User.id == user_id).first()

    game_word.users.remove(user)

    db.session.commit()

    return True
