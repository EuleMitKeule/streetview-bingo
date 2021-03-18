""" Module that includes methods serving the Angular-frontend files """
from flask import send_from_directory, current_app


@current_app.route("/<path:filename>", methods=["GET"])
def serve_file(filename: str):
    content_type = 'application/javascript'
    if filename == "index.html":
        content_type = 'text/html'
    return send_from_directory("../frontend/dist/frontend/", filename), {'content-type': content_type}


@current_app.route("/", methods=["GET"])
def serve_root():
    return serve_file(filename="index.html")
