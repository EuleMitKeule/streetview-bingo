

def test_get_lobby_by_id(mock_streetview_bingo):
    import services.lobby_service as lobby_service
    import services.user_service as user_service

    owner = user_service.create_user(name="eule")
    new_lobby = lobby_service.create_lobby(owner=owner)

    result = lobby_service.get_lobby(lobby_id=new_lobby.id)

    assert result.owner.name == owner.name


def test_get_lobby_by_token(mock_streetview_bingo):
    import services.lobby_service as lobby_service
    import services.user_service as user_service

    owner = user_service.create_user(name="eule")
    new_lobby = lobby_service.create_lobby(owner=owner)

    result = lobby_service.get_lobby(lobby_token=new_lobby.token)

    assert result.owner.name == owner.name


def test_get_lobby_by_none(mock_streetview_bingo):
    import services.lobby_service as lobby_service
    import services.user_service as user_service

    owner = user_service.create_user(name="eule")
    lobby_service.create_lobby(owner=owner)

    result = lobby_service.get_lobby()

    assert result is None


def test_create_lobby(mock_streetview_bingo):
    import services.lobby_service as lobby_service
    import services.user_service as user_service

    owner = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)

    assert lobby.owner == owner
    assert owner in lobby.users
    assert lobby.token is not None
    assert len(lobby.games) == 0


def test_delete_lobby(mock_streetview_bingo):
    import services.lobby_service as lobby_service
    import services.user_service as user_service

    owner = user_service.create_user(name="eule")
    user = user_service.create_user(name="affe")
    lobby = lobby_service.create_lobby(owner=owner)
    lobby_service.join_lobby(user=user, lobby_token=lobby.token)

    lobby_service.delete_lobby(lobby_id=lobby.id)

    result = lobby_service.get_lobby(lobby_id=lobby.id)
    owner = user_service.get_user(user_token=owner.token)
    user = user_service.get_user(user_token=user.token)

    assert result is None
    assert owner is None
    assert user is None


def test_join_lobby(mock_streetview_bingo):
    import services.lobby_service as lobby_service
    import services.user_service as user_service

    owner = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)

    user = user_service.create_user(name="affe")
    lobby_service.join_lobby(user=user, lobby_token=lobby.token)

    assert user in lobby.users

    lobby_service.join_lobby(user=user, lobby_token=lobby.token)

    assert len(lobby.users) == 2
