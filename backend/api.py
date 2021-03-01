import connexion
from flask_cors import CORS
from flask import Flask
from sqlalchemy.sql.expression import func
import config
from models import Word, WordSchema
from flask.json import jsonify

def create_lobby():
    pass


def get_lobby():
    pass


def join_lobby():
    pass


def create_game():
    pass


def update_game():
    pass


def create_word_status():
    pass


def delete_word_status():
    pass


def get_words(length):

    words = Word.query.order_by(func.random()).limit(length).all()
    word_schema = WordSchema(many=True)
    result = jsonify(word_schema.dump(words))

    return result


if __name__ == "__main__":
    connex_app = config.connex_app
    CORS(connex_app.app)
    connex_app.add_api('openapi.yaml', strict_validation=True, validate_responses=True, base_path="/api")
    connex_app.add_api('angular.yaml', options={"swagger_ui": False})
    connex_app.run()