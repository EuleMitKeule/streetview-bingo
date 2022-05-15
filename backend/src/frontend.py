""" Module that includes methods serving the Angular-frontend files """
from flask import Blueprint, send_from_directory

frontend_bp = Blueprint("frontend", __name__, url_prefix="/")


@frontend_bp.route("/<filename>", methods=["GET"])
def serve_file(filename: str):
    if filename == "":
        filename = "index.html"
    return send_from_directory("../../frontend/dist/frontend/", filename)


@frontend_bp.route("", methods=["GET"])
def serve_root():
    return serve_file("index.html")
