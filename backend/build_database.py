import os
from config import db
from models import Word

sample_words = [
    "Dog",
    "Car",
    "Stoplight"
]

if os.path.exists('streetview-bingo.db'):
    os.remove('streetview-bingo.db')

db.create_all()

for sample_word in sample_words:
    word = Word(text=sample_word)
    db.session.add(word)

db.session.commit()