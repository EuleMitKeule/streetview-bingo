from flask import current_app

db = current_app.db

word_user_table = db.Table(
    'word_user', db.Model.metadata,
    db.Column('word_id', db.Integer, db.ForeignKey('game_word.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)


class Word(db.Model):
    __tablename__ = "word"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), index=True)
