from flask_socketio import join_room, leave_room
from common import *


@sio.on("join")
def on_join(data):
    room = data["room"]
    join_room(room)


@sio.on("leave")
def on_leave(data):
    room = data["room"]
    leave_room(room)
