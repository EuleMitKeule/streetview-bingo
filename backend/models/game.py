from flask import current_app

db = current_app.db

game_user_table = db.Table(
    'game_user', db.Model.metadata,
    db.Column('game_id', db.Integer, db.ForeignKey('game.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)


class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(16), index=True)
    status = db.Column(db.String(16))
    moderator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    users = db.relationship("User", secondary=game_user_table)
    words = db.relationship("GameWord", backref="game", foreign_keys='GameWord.game_id')
    lobby_id = db.Column(db.Integer, db.ForeignKey("lobby.id"))