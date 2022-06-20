import werkzeug
from .request_handler import RequestHandler

setattr(werkzeug.serving.WSGIRequestHandler, "log", RequestHandler.log)
setattr(werkzeug.serving.WSGIRequestHandler, "log_request", RequestHandler.log_request)
