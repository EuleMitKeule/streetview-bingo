import connexion
from flask_cors import CORS


def hello():
    return [
        {
            "text": "test123"
        },
        {
            "text": "test345"
        }
    ]


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=5000, specification_dir='config')
    app.add_api('angular.yaml', options={"swagger_ui": False})
    CORS(app.app)
    app.run()