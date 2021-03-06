import yaml
from os import path
import logging

from streetview_bingo import StreetViewBingo
from config.config import Config
from config.database_config import DatabaseConfig, MysqlConfig, SqliteConfig

if __name__ == '__main__':

    basedir: str = path.abspath(path.dirname(__file__))

    conf_path: str = path.join(basedir, "streetview-bingo.conf")
    config: Config = Config()

    print("Loading configuration from file: " + conf_path)

    if not path.exists(conf_path):
        print("ERROR - No configuration file found.")
        quit()

    with open(conf_path, "r") as conf_file:
        conf_dict = yaml.load(conf_file, Loader=yaml.FullLoader)

    # # # Logging Configuration # # #

    if "logging" in conf_dict:
        print("Found logging configuration.")

        if "path" in conf_dict["logging"]:
            config.log_path = conf_dict["logging"]["path"]

        if "level" in conf_dict["logging"]:
            log_level = conf_dict["logging"]["level"]

            if log_level == "debug":
                config.log_level = logging.DEBUG
            if log_level == "info":
                config.log_level = logging.INFO
            if log_level == "warning":
                config.log_level = logging.WARNING
            if log_level == "error":
                config.log_level = logging.ERROR

        logging.basicConfig(
            filename=config.log_path,
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=config.log_level
        )

    # # # Database Configuration # # #

    if "database" not in conf_dict:
        logging.error("Could not find database configuration.")
        quit()

    logging.info("Found database configuration.")

    if "type" not in conf_dict["database"]:
        logging.error("Database type not specified.")
        quit()

    database_type: str = conf_dict["database"]["type"]

    if database_type not in DatabaseConfig.database_types:
        logging.error(f"Database type not recognized.\nRecognized types are: {DatabaseConfig.database_types}")
        quit()

    logging.info(f"Using database type: {database_type}")

    database_config: DatabaseConfig = None

    if database_type == "sqlite":
        if "path" not in conf_dict["database"]:
            logging.error("SQLite database path not specified.")
            quit()

        db_path = path.realpath(conf_dict["database"]["path"])

        logging.info(f"Using SQLite database file at: {db_path}")

        database_config = SqliteConfig(path=db_path)

    if database_type == "mysql":
        if "host" not in conf_dict["database"]:
            logging.error("MySQL host not specified.")
            quit()
        if "port" not in conf_dict["database"]:
            logging.error("MySQL port not specified.")
            quit()
        if "user" not in conf_dict["database"]:
            logging.error("MySQL username not specified.")
            quit()
        if "pass" not in conf_dict["database"]:
            logging.error("MySQL password not specified.")
            quit()
        if "db_name" not in conf_dict["database"]:
            logging.error("MySQL database name not specified.")
            quit()

        db_host = conf_dict["database"]["host"]
        db_port = conf_dict["database"]["port"]
        db_user = conf_dict["database"]["user"]
        db_pass = conf_dict["database"]["pass"]
        db_name = conf_dict["database"]["db_name"]

        logging.info(f"Using MySQL database at {db_host}:{db_port}")

        database_config = MysqlConfig(
            host=db_host,
            port=db_port,
            username=db_user,
            password=db_pass,
            db_name=db_name
        )

    config.database_config = database_config

    streetview_bingo = StreetViewBingo(config)
    streetview_bingo.run()
