APP_NAME = "flask-template"
APP_VERSION = "0.0.0"

DEFAULT_CONFIG_PATH = "config/config.yml"
DEFAULT_LOG_PATH = "logs/app.log"
DEFAULT_SQLITE_PATH = "data/app.sqlite"
DEFAULT_SPEC_PATH = "openapi.json"

DEFAULT_LOG_LEVEL = "DEBUG"
DEFAULT_LOG_FORMAT = "[%(asctime)s] (%(name)s) %(levelname)s %(message)s"
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_LOG_STREAM = "sys.stderr"
DEFAULT_LOG_MAX_SIZE = 1_000_000
DEFAULT_LOG_MAX_FILES = 3
DEFAULT_LOG_PROPAGATE = True

DEFAULT_PORT = 5000
DEFAULT_HOST = "localhost"

DEFAULT_SECRET_KEY = "changeme"

DEFAULT_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
DEFAULT_REDOC_URL = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"