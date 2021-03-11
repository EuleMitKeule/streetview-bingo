import logging


class DatabaseConfig:
    database_types = ["sqlite", "mysql"]
    database_type: str = None


class SqliteConfig(DatabaseConfig):
    path: str = None
    recreate: bool = False

    def __init__(self, path, recreate=False):
        self.path = path
        self.recreate = recreate


class MysqlConfig(DatabaseConfig):
    host: str = None
    port: int = None
    username: str = None
    password: str = None
    db_name: str = None

    def __init__(self, host: str, port: int, username: str, password: str, db_name: str):
        if port < 1 or port > 65535:
            logging.error("Specified port is not inside range of possible ports.")
            quit()

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name
