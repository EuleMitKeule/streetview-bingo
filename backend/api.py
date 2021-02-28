import connexion
from flask import send_from_directory
from flask_cors import CORS

def serve_file(filename: str):
    if filename == "":
        filename = "index.html"
    return send_from_directory("../frontend/dist/frontend/", filename)


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
    app.add_api('openapi.yaml', strict_validation=True, validate_responses=True, base_path="/api")
    app.add_api('angular.yaml')
    CORS(app.app)
    app.run()