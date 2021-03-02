from config import connex_app, db
from models import Word, GameWord, Lobby, User, Game
from sqlalchemy.sql.expression import func


def get_random_words(length):
    words = Word.query.order_by(func.random()).limit(length).all()
    return words


def set_word_found(lobby_token, game_token, user_token, word_id, user_id):
    
    lobby = Lobby.query.filter(Lobby.token==lobby_token).first()
    game = Game.query.filter(Game.token==game_token).first()

    if game.moderator.token != user_token:
        return False

    game_word = GameWord.query.filter(GameWord.id==word_id).first()
    user = User.query.filter(User.id==user_id).first()
    
    game_word.users.append(user)

    db.session.commit()

    return True


def set_word_not_found(lobby_token, game_token, user_token, word_id, user_id):
    
    lobby = Lobby.query.filter(Lobby.token==lobby_token).first()
    game = Game.query.filter(Game.token==game_token).first()

    if game.moderator.token != user_token:
        return False

    game_word = GameWord.query.filter(GameWord.id==word_id).first()
    user = User.query.filter(User.id==user_id).first()
    
    game_word.users.remove(user)

    db.session.commit()

    return True