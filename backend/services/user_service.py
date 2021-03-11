from flask import current_app
from models.user import User
import services.token_service as token_service


db = current_app.db


def get_user(user_id: int = None, user_token: str = None):
    """
    Returns a user from the user database.

    :param user_token: The token of the user to return.
    :param user_id: The ID of the user to return.
    :return: The user if found.
    """
    if user_id is not None:
        return User.query.filter(User.id == user_id).first()
    elif user_token is not None:
        return User.query.filter(User.token == user_token).first()
    else:
        return None


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
    User.query.filter(User.id == user_id).delete()

    db.session.commit()
