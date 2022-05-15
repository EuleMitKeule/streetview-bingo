

class NetworkingConfig:
    host: str
    port: int

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
