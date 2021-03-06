import os
from connexion import FlaskApp
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask import current_app


class StreetViewBingo:
    connex_app: FlaskApp = None
    db: SQLAlchemy = None
    ma: Marshmallow = None

    def __init__(self):
        basedir: str = os.path.abspath(os.path.dirname(__file__))
        db_path: str = os.path.join(basedir, 'streetview-bingo.db')

        self.connex_app = FlaskApp(__name__, port=5000, specification_dir='config')

        with self.connex_app.app.app_context():
            self.connex_app.app.config['SQLALCHEMY_ECHO'] = True
            self.connex_app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
            self.connex_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

            self.db = SQLAlchemy(self.connex_app.app)
            self.ma = Marshmallow(self.connex_app.app)

            current_app.db = self.db
            current_app.ma = self.ma

            self.connex_app.add_api('openapi.yaml', strict_validation=True, validate_responses=True, base_path="/api")
            self.connex_app.add_api('angular.yaml', options={"swagger_ui": False})

            CORS(self.connex_app.app)

        if not os.path.exists(db_path):
            self.create_db()

    def run(self):
        self.connex_app.run()

    def create_db(self):
        self.db.create_all()

