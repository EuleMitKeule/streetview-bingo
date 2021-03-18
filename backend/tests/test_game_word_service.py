

def test_get_game_word_by_id(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    import services.game_word_service as game_word_service
    from models.game_word import GameWord

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    game_word = game_word_service.create_game_word(text="Dog", game_token=game.token)

    result: GameWord = game_word_service.get_game_word(game_word_id=game_word.id)

    assert result.id == game_word.id
    assert result.game_id == game.id
    assert result.text == "Dog"


def test_get_game_word_by_content_and_id(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    import services.game_word_service as game_word_service
    from models.game_word import GameWord

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    game_word = game_word_service.create_game_word(text="Dog", game_token=game.token)

    result: GameWord = game_word_service.get_game_word_by_content(text="Dog", game_id=game.id)

    assert result.id == game_word.id
    assert result.game_id == game.id
    assert result.text == "Dog"


def test_get_game_word_by_content_and_token(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    import services.game_word_service as game_word_service
    from models.game_word import GameWord

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    game_word = game_word_service.create_game_word(text="Dog", game_token=game.token)

    result: GameWord = game_word_service.get_game_word_by_content(text="Dog", game_token=game.token)

    assert result.id == game_word.id
    assert result.game_id == game.id
    assert result.text == "Dog"


def test_get_game_word_by_none(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    import services.game_word_service as game_word_service
    from models.game_word import GameWord

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    game_word_service.create_game_word(text="Dog", game_token=game.token)

    result: GameWord = game_word_service.get_game_word_by_content(text="Dog")

    assert result is None


def test_create_game_word(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    import services.game_word_service as game_word_service

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    game_word = game_word_service.create_game_word(text="Catdog", game_token=game.token)

    assert len(game_word.users) == 0
    assert game_word.text == "Catdog"
    assert game_word.game_id == game.id
    assert game_word in game.words
    assert len(game.words) == 1


def test_create_empty(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    import services.game_word_service as game_word_service

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    game_word = game_word_service.create_game_word(text="  / 12@**#", game_token=game.token)

    assert game_word is None


def test_delete_game_word(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    import services.game_word_service as game_word_service

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    game_word = game_word_service.create_game_word(text="Goose", game_token=game.token)

    game_word_service.delete_word(game_token=game.token, text=game_word.text)

    game_word = game_word_service.get_game_word(game_word_id=game_word.id)

    assert game_word is None
    assert len(game.words) == 0


def test_set_found(mock_streetview_bingo):
    import services.user_service as user_service
    import services.lobby_service as lobby_service
    import services.game_service as game_service
    import services.game_word_service as game_word_service

    owner = user_service.create_user(name="eule")
    moderator = user_service.create_user(name="eule")
    lobby = lobby_service.create_lobby(owner=owner)
    game = game_service.create_game(lobby_token=lobby.token, moderator_id=moderator.id)

    game_word = game_word_service.create_game_word(text="Duckling", game_token=game.token)

    game_word_service.set_found(
        game_token=game.token,
        user_token=moderator.token,
        game_word_id=game_word.id,
        user_id=owner.id
    )

    assert owner in game_word.users

    game_word_service.set_not_found(
        game_token=game.token,
        user_token=moderator.token,
        game_word_id=game_word.id,
        user_id=owner.id
    )

    assert owner not in game_word.users

    game_word = game_word_service.create_game_word(text="Goosling", game_token=game.token)

    game_word_service.set_found(
        game_token=game.token,
        user_token=owner.token,
        game_word_id=game_word.id,
        user_id=owner.id
    )

    assert owner not in game_word.users

    game_word = game_word_service.get_game_word_by_content(text="Duckling", game_token=game.token)

    game_word_service.set_found(
        game_token=game.token,
        user_token=moderator.token,
        game_word_id=game_word.id,
        user_id=owner.id
    )

    game_word_service.set_not_found(
        game_token=game.token,
        user_token=owner.token,
        game_word_id=game_word.id,
        user_id=owner.id
    )

    assert owner in game_word.users
