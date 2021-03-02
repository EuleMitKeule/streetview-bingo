from config import db
from models import Game, Lobby, User
import services.token_service as token_service


def create_game(moderator_id):

    token = token_service.generate_token(16)
    moderator = User.query().filter(User.id==moderator_id).first()
    game = Game(
        token=token,
        status="created",
        moderator=moderator)

    lobby = Lobby.query().filter(Lobby.id==moderator.lobby_id).first()
    game.users = lobby.users

    db.session.add(game)
    db.session.commit()

    return game