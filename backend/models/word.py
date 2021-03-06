from flask import current_app


db = current_app.db


class Word(db.Model):
    __tablename__ = "word"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), index=True)
