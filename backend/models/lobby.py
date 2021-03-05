from flask import current_app

db = current_app.db


class Lobby(db.Model):
    __tablename__ = "lobby"
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship("User", backref="lobby", foreign_keys='User.lobby_id')
    owner = db.relationship("User", backref="owned_lobby", uselist=False, foreign_keys='User.owned_lobby_id')
    token = db.Column(db.String(16), index=True)
    games = db.relationship("Game", backref="games", foreign_keys="Game.lobby_id")
