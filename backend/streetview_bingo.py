from connexion import FlaskApp
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask import current_app

from config.config import Config
from config.database_config import SqliteConfig, MysqlConfig


class StreetViewBingo:
    connex_app: FlaskApp = None
    db: SQLAlchemy = None
    ma: Marshmallow = None
    config: Config = None

    def __init__(self, config: Config):

        self.connex_app = FlaskApp(__name__, port=5000, specification_dir='specification')
        self.config = config

        with self.connex_app.app.app_context():

            self.connex_app.app.config['SQLALCHEMY_ECHO'] = True
            self.connex_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

            if type(config.database_config) is SqliteConfig:
                sqlite_config = config.database_config
                self.connex_app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sqlite_config.path

            if type(config.database_config) is MysqlConfig:
                mysql_config = config.database_config
                self.connex_app.app.config['SQLALCHEMY_DATABASE_URI'] = \
                    f"mysql:///{mysql_config.username}:{mysql_config.password}@" \
                    f"{mysql_config.host}:{mysql_config.port}/{mysql_config.db_name}"

            self.db = SQLAlchemy(self.connex_app.app)
            self.ma = Marshmallow(self.connex_app.app)

            current_app.db = self.db
            current_app.ma = self.ma

            self.connex_app.add_api('openapi.yaml', strict_validation=True, validate_responses=True, base_path="/api")
            self.connex_app.add_api('angular.yaml', options={"swagger_ui": False})

            CORS(self.connex_app.app)

        self.create_db()

    def run(self):
        self.connex_app.run()

    def create_db(self):
        if type(self.config.database_config) is SqliteConfig:
            sqlite_config = self.config.database_config
            if sqlite_config.recreate:
                self.db.drop_all()
        self.db.create_all()
