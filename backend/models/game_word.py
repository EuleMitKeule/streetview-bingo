from flask import current_app

db = current_app.db


class GameWord(db.Model):
    __tablename__ = "game_word"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), index=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    users = db.relationship("User", secondary=word_user_table)