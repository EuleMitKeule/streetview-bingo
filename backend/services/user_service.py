from config import db
from models import User
import services.token_service as token_service


def get_user_by_id(user_id: int):
    """
    Returns a user from the user database.

    :param user_id: The ID of the user to return.
    :return: The user if found.
    """
    user = User.query.filter(User.id == user_id).first()

    return user


def get_user_by_token(user_token: str):
    """
    Returns a user from the user database.

    :param user_token: The token of the user to return.
    :return: The user if found.
    """
    user = User.query.filter(User.token == user_token).first()

    return user


def create_user(name: str):
    """
    Creates a new user.

    :param name: The name of the user.
    :return: The created user if successful.
    """
    token = token_service.generate_token(16)
    user = User(name=name, token=token)

    db.session.add(user)

    db.session.commit()
    return user


def delete_user(user_id: int):
    """
    Deletes a user from the user database.

    :param user_id: The ID of the user to delete
    """
    user = get_user_by_id(user_id)
    user.delete()

    db.session.commit()
