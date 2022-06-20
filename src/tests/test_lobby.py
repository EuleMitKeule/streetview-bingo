

def test_lobby():

    from src.models import User, Lobby, Word
    from src.common import db

    user: User = User.create(name="eule")
    assert user

    lobby: Lobby = Lobby.create(users=[user], owner=user)
    assert lobby
    assert user in lobby.users
