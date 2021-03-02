from config import db
from models import Lobby
import services.token_service as token_service


def get_lobby(token):
    lobby = Lobby.query.filter(Lobby.token==token).first()
    return lobby


def create_lobby(owner):
    
    token = token_service.generate_token(16)
    lobby = Lobby(owner=owner, token=token)
    lobby.users.append(owner)

    db.session.add(lobby)
    db.session.commit()

    return lobby


def join_lobby(user, token):

    lobby = Lobby.query.filter(Lobby.token==token).first()
    lobby.users.append(user)
    
    db.session.commit()