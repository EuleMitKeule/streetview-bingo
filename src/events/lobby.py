from src.common import sio


@sio.on("reload")
def on_reload(data):
    room = data["room"]
    sio.emit("reload", data, room=room, include_self=False)


@sio.on("lobby_moderator_update")
def on_lobby_moderator_update(data):
    room = data["room"]
    sio.emit("lobby_moderator_update", data, room=room, include_self=False)

@sio.on("game_word_found")
def on_game_word_found(data):
    room = data["room"]
    sio.emit("game_word_found", data, room=room, include_self=False)

@sio.on("game_map_sync")
def on_game_map_sync(data):
    room = data["room"]
    sio.emit("game_map_sync", data, room=room, include_self=False)