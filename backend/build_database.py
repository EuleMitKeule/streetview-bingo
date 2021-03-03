import os
from config import db
from models import Word, User, Lobby, Game, GameWord


if os.path.exists('streetview-bingo.db'):
    os.remove('streetview-bingo.db')

db.create_all()

db.session.add(Word())
db.session.add(User())
db.session.add(Lobby())
db.session.add(Game())
db.session.add(GameWord())

db.session.commit()
