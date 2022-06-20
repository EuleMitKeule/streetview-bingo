from typing import Any, Union
from werkzeug.serving import WSGIRequestHandler
from werkzeug.urls import uri_to_iri
from werkzeug._internal import _log


class RequestHandler(WSGIRequestHandler):
    def log(self, type: str, message: str, *args: Any) -> None:
        _log(
            type,
            message,
            *args
        )

    def log_request(self, code: Union[int, str] = "-", size: Union[int, str] = "-") -> None:
        try:
            path = uri_to_iri(self.path)
            msg = f"{self.command} {path}"
        except AttributeError:
            msg = self.requestline

        code = str(code)
        self.log("info", f"{msg} {code}")
