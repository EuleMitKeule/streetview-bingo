from config import db
from models import Game, Lobby, User, GameWord
import services.token_service as token_service


def create_game(lobby_token, moderator_id):

    token = token_service.generate_token(16)
    moderator = User.query.filter(User.id==moderator_id).first()
    game = Game(
        token=token,
        status="created",
        moderator=moderator)

    lobby = Lobby.query.filter(Lobby.token==lobby_token).first()
    game.users = lobby.users

    db.session.add(game)
    db.session.commit()

    return game


def update_game(lobby_token, game_token, user_token, body):

    game = Game.query.filter(Game.token==game_token).first()

    if game.moderator.token != user_token:
        return None

    if 'status' in body:
        game.status = body['status']

    game_words = []

    for word_dict in body['words']:
        text = word_dict['text']
        game_word = GameWord(text=text)
        db.session.add(game_word)
        game_words.append(game_word)

    game.words = game_words

    return game