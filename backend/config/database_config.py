import logging


class DatabaseConfig:
    database_types = ["sqlite", "mysql", "postgresql"]
    database_type: str = None


class SqliteConfig(DatabaseConfig):
    path: str = None

    def __init__(self, path):
        self.path = path


class MysqlConfig(DatabaseConfig):
    host: str = None
    port: int = None

    def __init__(self, host, port):
        if port < 1 or port > 65535:
            logging.error("Specified port is not inside range of possible ports.")
            quit()

        self.host = host
        self.port = port
