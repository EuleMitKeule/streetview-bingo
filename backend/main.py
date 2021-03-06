import yaml
from os import path
import logging
from streetview_bingo import StreetViewBingo
from config import Config

if __name__ == '__main__':

    basedir: str = path.abspath(path.dirname(__file__))
    log_path: str = path.join(basedir, 'streetview-bingo.log')

    logging.basicConfig(
        filename=log_path,
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.DEBUG
    )

    conf_path: str = path.join(basedir, "streetview-bingo.conf")

    if not path.exists(conf_path):
        logging.warning("No configuration file found.")

        with open(conf_path, "w") as conf_file:
            # TODO Write defaults to conf file
            quit()

    else:
        logging.info(f"Loading configuration from file.")

        with open(conf_path, "r") as conf_file:
            conf = yaml.load(conf_file, Loader=yaml.FullLoader)

        if "database" not in conf:
            logging.error("Could not find database configuration.")
            quit()

        logging.info("Found database configuration.")

        if "type" not in conf["database"]:
            logging.error("Database type not specified.")
            quit()

        database_type: str = conf["database"]["type"]

        if database_type not in Config.database_types:
            logging.error(f"Database type not recognized.\nRecognized types are: {Config.database_types}")
            quit()

        logging.info(f"Using database type: {database_type}")

        if database_type == "sqlite":
            if "path" not in conf["database"]:
                logging.error("SQLite database path not specified.")
                quit()

            db_path = path.realpath(conf["database"]["path"])

            logging.info(f"Using SQLite database file at: {db_path}")

    streetview_bingo = StreetViewBingo()
    streetview_bingo.run()
