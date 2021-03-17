

def test_get_game_by_id(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    from models.game import Game

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    result: Game = game_service.get_game(game_id=game.id)

    assert result is not None
    assert result.lobby_id == lobby.id
    assert result.token is not None
    assert owner in result.users
    assert moderator not in result.users
    assert result.moderator_id == moderator.id
    assert len(result.words) == 0


def test_get_game_by_token(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    from models.game import Game

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    result: Game = game_service.get_game(game_token=game.token)

    assert result is not None
    assert result.lobby_id == lobby.id
    assert result.token is not None
    assert owner in result.users
    assert moderator not in result.users
    assert result.moderator_id == moderator.id
    assert len(result.words) == 0


def test_get_game_by_none(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    from models.game import Game

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    result: Game = game_service.get_game()

    assert result is None


def test_create_game(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    from models.game import Game

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game: Game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    assert game.lobby_id == lobby.id
    assert game.token is not None
    assert owner in game.users
    assert moderator not in game.users
    assert game.moderator_id == moderator.id
    assert len(game.words) == 0
    assert len(lobby.games) == 1


def test_delete_game(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    game_service.delete_game(game_token=game.token)

    game = game_service.get_game(game_id=game.id)

    assert game is None
    assert len(lobby.games) == 0


def test_update_game(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    from models.game import Game

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game: Game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    assert game.status == "created"

    game = game_service.update_game(
        game_token=game.token,
        user_token=moderator.token,
        status="running",
        texts=["Dog", "Stoplight"]
    )

    assert game.status == "running"
    assert len(game.words) == 2

    game = game_service.update_game(
        game_token=game.token,
        user_token=moderator.token,
        texts=["Cat", "Dog"]
    )

    assert len(game.words) == 3

    game = game_service.update_game(
        game_token=game.token,
        user_token=owner.token,
        status="stopped",
        texts=["Car"]
    )

    assert game is None


def test_is_moderator(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    is_mod = game_service.is_moderator(game_token=game.token, user_token=owner.token)

    assert not is_mod

    is_mod = game_service.is_moderator(game_token=game.token, user_token=moderator.token)

    assert is_mod
