import logging

from connexion import FlaskApp
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask import current_app
from flask_socketio import SocketIO, emit, send
from threading import Thread

from config.config import Config
from config.database_config import SqliteConfig, MysqlConfig


class StreetViewBingo:
    connex_app: FlaskApp = None
    db: SQLAlchemy = None
    ma: Marshmallow = None
    config: Config = None

    def __init__(self, config: Config):

        self.connex_app = FlaskApp(__name__, host="0.0.0.0", port=5000, specification_dir='specification')
        self.config = config

        with self.connex_app.app.app_context():

            self.connex_app.app.config['SQLALCHEMY_ECHO'] = False
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
            self.socketio = SocketIO(self.connex_app.app, cors_allowed_origins="*")

            current_app.streetview_bingo = self
            current_app.db = self.db
            current_app.ma = self.ma

            self.connex_app.add_api('openapi.yaml', strict_validation=True, validate_responses=True, base_path="/api")
            import frontend

            CORS(self.connex_app.app)

        self.create_db()

    def run(self):
        # self.connex_app.run()
        logging.getLogger('socketio').setLevel(logging.INFO)
        self.socketio.run(app=self.connex_app.app, debug=True)

    def create_db(self):
        if type(self.config.database_config) is SqliteConfig:
            sqlite_config = self.config.database_config
            if sqlite_config.recreate:
                self.db.drop_all()
        self.db.create_all()
