""" Module that includes methods serving the Angular-frontend files """
from flask import send_from_directory

def serve_file(filename: str):
    if filename == "":
        filename = "index.html"
    return send_from_directory("../frontend/dist/frontend/", filename)

def serve_root():
    return serve_file("index.html")
