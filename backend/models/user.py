from flask import current_app

db = current_app.db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    token = db.Column(db.String(16), index=True)
    lobby_id = db.Column(db.Integer, db.ForeignKey("lobby.id"))
    owned_lobby_id = db.Column(db.Integer, db.ForeignKey("lobby.id"))
    moderated_games = db.relationship("Game", backref="moderator", foreign_keys='Game.moderator_id')