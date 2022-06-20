import os
from flask import Blueprint, send_from_directory


bp: Blueprint = Blueprint("frontend", __name__, url_prefix="/")


@bp.route("/<filename>", methods=["GET"])
def serve_file(filename: str):
    if filename == "":
        filename = "index.html"

    path = os.path.abspath(os.path.join('frontend/build/', filename))
    print(f"Serving {path}")
    print(f"{os.path.exists(path)}")

    return send_from_directory(os.path.abspath("frontend/build/"), filename)


@bp.route("/static/js/<filename>", methods=["GET"])
def serve_js_file(filename: str):
    return send_from_directory(os.path.abspath("frontend/build/static/js"), filename)


@bp.route("/static/css/<filename>", methods=["GET"])
def serve_css_file(filename: str):
    return send_from_directory(os.path.abspath("frontend/build/static/css"), filename)


@bp.route("", methods=["GET"])
def serve_root():
    return serve_file("index.html")
