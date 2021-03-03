from config import db
from models import Game, User, GameWord
import game_service


def set_word_found(game_token, user_token, word_id, user_id):
    game = Game.query.filter(Game.token == game_token).first()

    if game.moderator.token != user_token:
        return False

    game_word = GameWord.query.filter(GameWord.id == word_id).first()
    user = User.query.filter(User.id == user_id).first()

    game_word.users.append(user)

    db.session.commit()

    return True


def set_word_not_found(game_token, user_token, word_id, user_id):
    game = game_service.get_game(game_token)

    if game.moderator.token != user_token:
        return False

    game_word = GameWord.query.filter(GameWord.id == word_id).first()
    user = User.query.filter(User.id == user_id).first()

    game_word.users.remove(user)

    db.session.commit()

    return True
