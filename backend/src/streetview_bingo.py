import os
from argparse import ArgumentParser
from flask import Flask

from common import *
from models import *
from api import bp

def create_app(config_path: str) -> Flask:
    app = Flask(__name__)
    
    config.load(config_path)

    db_folder: str = os.path.dirname(os.path.abspath(config.config_model.sqlite.db_path))

    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + config.config_model.sqlite.db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = config.config_model.secret_key

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    sio.init_app(app, cors_allowed_origins="*")

    with app.app_context():
        BaseModel.set_session(db.session)

        if config.config_model.sqlite.recreate:
            logging.info("Recreating database")
            db.drop_all()
            db.session.commit()

        db.create_all()
        db.session.commit()

    app.register_blueprint(bp)

    return app

if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-c", "--config", dest="config_path", help="The path to the configuration file.")
    args = arg_parser.parse_args()
    config_path = args.config_path if args.config_path else "../config/streetview-bingo.yml"
    
    app: Flask = create_app(config_path)
    sio.run(app, host=config.config_model.networking.host, port=config.config_model.networking.port)
