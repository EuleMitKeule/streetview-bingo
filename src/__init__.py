from flask import Flask

from src.common import config, db, ma, cors, sio, scheduler, api, csrf
from src.const import APP_NAME
import src.patches


app = Flask(__name__)

config.init_app(app)
cors.init_app(app)
db.init_app(app)
ma.init_app(app)
api.init_app(app)
sio.init_app(app, cors_allowed_origins="*")
scheduler.init_app(app)
csrf.init_app(app)

import src.models
import src.views
import src.events
from src.blueprints import frontend_bp
from src.models import BaseModel

with app.app_context():
    BaseModel.set_session(db.session)

    if config.config_model.sqlite.recreate:
        app.logger.info("Recreating database...")
        db.drop_all()
        db.session.commit()

    db.create_all()
    db.session.commit()

app.register_blueprint(frontend_bp)

scheduler.start()

app.logger.info(f"{APP_NAME} initialized.")
