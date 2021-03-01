import connexion
from flask_cors import CORS


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

def get_words():
    pass


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=5000, specification_dir='config')
    app.add_api('openapi.yaml', strict_validation=True, validate_responses=True, base_path="/api")
    app.add_api('angular.yaml', options={"swagger_ui": False})
    CORS(app.app)
    app.run()