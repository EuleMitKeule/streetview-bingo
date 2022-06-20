import pytest

from src.common import db, config

@pytest.fixture(autouse=True, scope="session")
def app():
    from src import app
    config.configure_test_logging()

    with app.app_context():
        db.session.commit()
    return app
  
@pytest.fixture(autouse=True, scope="function")
def recreate_db(app):
    with app.app_context():
        db.session.commit()
