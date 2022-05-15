from flask_socketio import SocketIO
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import *

    
igdb_token: str = ""
config: Config = Config()
db: SQLAlchemy = SQLAlchemy(session_options={
    'expire_on_commit': False
})
ma: Marshmallow = Marshmallow()
cors: CORS = CORS(cors_allowed_origins="*")
sio: SocketIO = SocketIO()
