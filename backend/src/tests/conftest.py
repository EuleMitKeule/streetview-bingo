
import pytest
from flask import Flask

from streetview_bingo import create_app
from common import db


def pytest_addoption(parser):
    parser.addoption(
        "--config",
        action="store",
        default="../config/test.config.yml",
        help="Path to config file"
    )

@pytest.fixture(scope="session")
def config_path(pytestconfig):
    return pytestconfig.getoption("--config")


@pytest.fixture(autouse=True, scope="function")
def mock_app(request, config_path):
    app: Flask = create_app(config_path)

    ctx = app.app_context()
    ctx.push()

    db.drop_all()
    db.create_all()
    db.session.commit()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app

