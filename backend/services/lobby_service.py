from flask import current_app
from models.lobby import Lobby
from models.user import User
import services.token_service as token_service


db = current_app.db


def get_lobby(lobby_id: int = None, lobby_token: str = None):
    """
    Returns a lobby from the lobby database.

    :param lobby_id: The ID of the lobby to return.
    :param lobby_token: The token of the lobby to return.
    :return: The lobby if found.
    """
    if lobby_id is not None:
        return Lobby.query.filter(Lobby.id == lobby_id).first()
    elif lobby_token is not None:
        return Lobby.query.filter(Lobby.token == lobby_token).first()
    else:
        return None


def create_lobby(owner: User):
    """
    Creates a new lobby.

    :param owner: The user owning the lobby.
    :return: The created lobby if successful.
    """
    token = token_service.generate_token(16)
    lobby = Lobby(owner=owner, token=token)

    lobby.users.append(owner)
    db.session.add(lobby)

    db.session.commit()
    return lobby


def delete_lobby(lobby_id: int):
    """
    Deletes a lobby from the lobby database.

    :param lobby_id: The ID of the lobby to delete.
    """
    lobby = Lobby.query.filter(Lobby.id == lobby_id).first()

    for user in lobby.users:
        User.query.filter(User.id == user.id).delete()

    Lobby.query.filter(Lobby.id == lobby_id).delete()
    db.session.commit()


def join_lobby(user: User, lobby_token: str):
    """
    Makes a user join a lobby.

    :param user: The user that should join the lobby.
    :param lobby_token: The token of the lobby to join.
    """
    lobby = get_lobby(lobby_token=lobby_token)

    if user not in lobby.users:
        lobby.users.append(user)
    
    db.session.commit()
