from common import *


@sio.on("connect")
def on_connection(data):
    print("Connected")
