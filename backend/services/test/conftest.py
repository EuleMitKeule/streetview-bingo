import pytest
from models import Word
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


@pytest.fixture
def mock_flask_app():
   mock_app = Flask(__name__)
   db = SQLAlchemy(mock_app)
   db.init_app(mock_app)
   return mock_app


@pytest.fixture
def mock_word():
    word = Word(id=1, text="Stoplight")
    return word


@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock