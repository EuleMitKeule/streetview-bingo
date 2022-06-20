from src.common import sio


@sio.on("connect")
def on_connection(data):
    print("Client connected")