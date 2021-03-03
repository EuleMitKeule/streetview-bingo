from config import db
from models import Lobby, User
import services.token_service as token_service


def get_lobby_by_token(lobby_token: str):
    """
    Returns a lobby from the lobby database.

    :param lobby_token: The token of the lobby to return.
    :return: The lobby if found.
    """
    lobby = Lobby.query.filter(Lobby.token == lobby_token).first()

    return lobby


def get_lobby_by_id(lobby_id: int):
    """
    Returns a lobby from the lobby database.

    :param lobby_id: The ID of the lobby to return.
    :return: The lobby if found.
    """
    lobby = Lobby.query.filter(Lobby.id == lobby_id).first()

    return lobby


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
    lobby = get_lobby_by_id(lobby_id)
    lobby.delete()
    db.session.commit()


def join_lobby(user: User, lobby_token: str):
    """
    Makes a user join a lobby.

    :param user: The user that should join the lobby.
    :param lobby_token: The token of the lobby to join.
    """
    lobby = get_lobby_by_token(lobby_token)
    lobby.users.append(user)
    
    db.session.commit()
