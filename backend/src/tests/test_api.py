from flask import jsonify


def test_create_lobby(mock_app, mocker):
    mocker.patch("models.TokenModel.generate_token", return_value="123")

    with mock_app.test_client() as client:
        json = {
            "username": "eule"
        }

        response = client.post("/api/lobby/", json=json)
        
        assert response.status_code == 200
        assert response.json == {
            "user": {
                "id": 1,
                "token": "123",
                "name": "eule"
            },
            "lobby": {
                "id": 1,
                "owner": {
                    "id": 1,
                    "name": "eule"
                },
                "users": [
                    {
                        "id": 1,
                        "name": "eule"
                    }
                ],
                "token": "123",
                "games": [],
            }
        }


def test_get_lobby(mock_app, mocker):
    test_create_lobby(mock_app, mocker)

    with mock_app.test_client() as client:
        response = client.get("/api/lobby/123")

        assert response.json == {
            "id": 1,
            "owner": {
                "id": 1,
                "name": "eule"
            },
            "users": [
                {
                    "id": 1,
                    "name": "eule"
                }
            ],
            "token": "123",
            "games": [],
        }
        assert response.status_code == 200


def test_join_lobby(mock_app, mocker):
    test_create_lobby(mock_app, mocker)

    mocker.patch("models.TokenModel.generate_token", return_value="321")

    with mock_app.test_client() as client:
        json = {
            "username": "schwein"
        }

        response = client.post("/api/lobby/123/join", json=json)

        assert response.status_code == 200
        assert response.json == {
            "id": 2,
            "name": "schwein",
            "token": "321",
        }


def test_create_game(mock_app, mocker):
    test_join_lobby(mock_app, mocker)

    mocker.patch("models.TokenModel.generate_token", return_value="123")

    with mock_app.test_client() as client:
        json = {
            "moderator": {
                "id": 1,
            }
        }

        response = client.post("/api/lobby/123/game/", json=json)

        assert response.status_code == 200
        assert response.json == {
            "id": 1,
            "token": "123",
            "status": "created",
            "users": [
                {
                    "id": 1,
                    "name": "eule"
                },
                {
                    "id": 2,
                    "name": "schwein"
                }
            ],
            "words": [],
            "moderator": {
                "id": 1,
                "name": "eule"
            }
        }


def test_get_game(mock_app, mocker):
    test_create_game(mock_app, mocker)

    with mock_app.test_client() as client:
        response = client.get("/api/lobby/123/game/123")

        assert response.status_code == 200
        assert response.json == {
            "id": 1,
            "token": "123",
            "status": "created",
            "users": [
                {
                    "id": 1,
                    "name": "eule"
                },
                {
                    "id": 2,
                    "name": "schwein"
                }
            ],
            "words": [],
            "moderator": {
                "id": 1,
                "name": "eule"
            }
        }


def test_update_game(mock_app, mocker):
    test_create_game(mock_app, mocker)

    with mock_app.test_client() as client:
        json = {
            "id": 1,
            "token": "123",
            "status": "running",
            "users": [
                {
                    "id": 1,
                    "name": "eule"
                },
                {
                    "id": 2,
                    "name": "schwein"
                }
            ],
            "words": [
                {
                    "text": "Dog"
                },
                {
                    "text": "Stoplight"
                }
            ],
            "moderator": {
                "id": 1,
                "name": "eule"
            }
        }

        response = client.put("/api/lobby/123/game/123?user_token=123", json=json)

        assert response.status_code == 200
        assert response.json == {
            "id": 1,
            "token": "123",
            "status": "running",
            "users": [
                {
                    "id": 1,
                    "name": "eule"
                },
                {
                    "id": 2,
                    "name": "schwein"
                }
            ],
            "words": [
                {
                    "id": 1,
                    "text": "Dog",
                    "users": []
                },
                {
                    "id": 2,
                    "text": "Stoplight",
                    "users": []
                }
            ],
            "moderator": {
                "id": 1,
                "name": "eule"
            }
        }


def test_create_word_status(mock_app, mocker):
    test_update_game(mock_app, mocker)

    with mock_app.test_client() as client:
        response = client.post("/api/lobby/123/game/123/words/1/users/2?user_token=123")

        assert response.status_code == 200

        response = client.get("/api/lobby/123/game/123")

        assert response.json == {
            "id": 1,
            "token": "123",
            "status": "running",
            "users": [
                {
                    "id": 1,
                    "name": "eule"
                },
                {
                    "id": 2,
                    "name": "schwein"
                }
            ],
            "words": [
                {
                    "id": 1,
                    "text": "Dog",
                    "users": [
                        {
                            "id": 2,
                            "name": "schwein"
                        }
                    ]
                },
                {
                    "id": 2,
                    "text": "Stoplight",
                    "users": []
                }
            ],
            "moderator": {
                "id": 1,
                "name": "eule"
            }
        }


def test_delete_word_status(mock_app, mocker):
    test_create_word_status(mock_app, mocker)

    with mock_app.test_client() as client:
        response = client.delete("/api/lobby/123/game/123/words/1/users/2?user_token=123")

        assert response.status_code == 200

        response = client.get("/api/lobby/123/game/123")

        assert response.json == {
            "id": 1,
            "token": "123",
            "status": "running",
            "users": [
                {
                    "id": 1,
                    "name": "eule"
                },
                {
                    "id": 2,
                    "name": "schwein"
                }
            ],
            "words": [
                {
                    "id": 1,
                    "text": "Dog",
                    "users": []
                },
                {
                    "id": 2,
                    "text": "Stoplight",
                    "users": []
                }
            ],
            "moderator": {
                "id": 1,
                "name": "eule"
            }
        }


def test_get_user(mock_app, mocker):
    test_delete_word_status(mock_app, mocker)

    with mock_app.test_client() as client:
        response = client.get("/api/users?user_token=321")

        assert response.status_code == 200
        assert response.json == {
            "id": 2,
            "name": "schwein",
            "token": "321"
        }
