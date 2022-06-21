from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
from flask_apscheduler import APScheduler
from flask_smorest import Api
from flask_praetorian import Praetorian
from flask_wtf import CSRFProtect

from src.config import Config


config: Config = Config()
    
cors: CORS = CORS(resources={r"/*": {"origins": "*", "send_wildcard": "False"}})

db: SQLAlchemy = SQLAlchemy(session_options={
    'expire_on_commit': False,
    "autocommit": True
})

ma: Marshmallow = Marshmallow()
sio: SocketIO = SocketIO()
scheduler: APScheduler = APScheduler()
api: Api = Api()
csrf: CSRFProtect = CSRFProtect()