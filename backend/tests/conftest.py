import pytest
from os import path

from config.database_config import SqliteConfig
from config.config import Config
from streetview_bingo import StreetViewBingo


@pytest.fixture(scope="module")
def mock_streetview_bingo():
    basedir: str = path.abspath(path.dirname(__file__))

    db_path = path.join(basedir, "test.db")
    db_config = SqliteConfig(path=db_path, recreate=True)
    config = Config()
    config.database_config = db_config

    streetview_bingo = StreetViewBingo(config=config)

    return streetview_bingo
