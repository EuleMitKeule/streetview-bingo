import os
from config import db
from models import Word, User, Lobby

sample_words = [
    "Dog",
    "Car",
    "Stoplight"
]

sample_users = [
    {"name": "eule", "token": "aaaaaaaaaaaaaaaa"},
    {"name": "affe", "token": "aaaaaaaaaaaaaaab"},
    {"name": "qualle", "token": "aaaaaaaaaaaaaaac"},
]

sample_lobbies = [
    {"token": "aaaaaaaaaaaaaaaa"}
]

if os.path.exists('streetview-bingo.db'):
    os.remove('streetview-bingo.db')

db.create_all()

for sample_word in sample_words:
    word = Word(text=sample_word)
    db.session.add(word)

for sample_user in sample_users:
    user = User(name=sample_user["name"], token=sample_user["token"])
    db.session.add(user)

for sample_lobby in sample_lobbies:
    lobby = Lobby(token=sample_lobby["token"])
    db.session.add(lobby)

db.session.commit()