from src.common import sio


@sio.on("reload")
def on_reload(data):
    room = data["room"]
    sio.emit("reload", data, room=room, include_self=False)


@sio.on("lobby_moderator_update")
def on_lobby_moderator_update(data):
    room = data["room"]
    sio.emit("lobby_moderator_update", data, room=room, include_self=False)