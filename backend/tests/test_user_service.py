

def test_get_user_by_id(mock_streetview_bingo):
    import services.user_service as user_service

    user_service.create_user(name="eule")
    new_user = user_service.create_user(name="affe")
    user_service.create_user(name="schwein")

    result = user_service.get_user(user_id=new_user.id)

    assert result.name == "affe"


def test_get_user_by_token(mock_streetview_bingo):
    import services.user_service as user_service

    new_user = user_service.create_user(name="eule")

    result = user_service.get_user(user_token=new_user.token)

    assert result.name == new_user.name


def test_get_user_by_none(mock_streetview_bingo):
    import services.user_service as user_service

    user_service.create_user(name="eule")

    result = user_service.get_user()

    assert result is None


def test_create_user(mock_streetview_bingo):
    import services.user_service as user_service
    from models.user import User

    new_user = user_service.create_user(name="eule")

    all_users = User.query.all()

    print(len(all_users))

    assert new_user.name == "eule"
    assert new_user.token is not None


def test_delete_user(mock_streetview_bingo):
    import services.user_service as user_service

    new_user = user_service.create_user(name="eule")
    user_service.delete_user(user_id=new_user.id)

    result = user_service.get_user(user_id=new_user.id)

    assert result is None
