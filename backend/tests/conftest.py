import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from os import path


@pytest.fixture
def mock_flask_app():
    basedir: str = path.abspath(path.dirname(__file__))
    mock_app = Flask(__name__)

    with mock_app.app_context():

        mock_app.config['SQLALCHEMY_ECHO'] = True
        mock_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        mock_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(basedir, "test.db")
        db = SQLAlchemy(mock_app)
        db.init_app(mock_app)

        current_app.db = db

        db.create_all()

    return mock_app
