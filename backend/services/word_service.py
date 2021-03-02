from config import connex_app, db
from models import Word, WordSchema
from sqlalchemy.sql.expression import func

def get_random_words(length):
    words = Word.query.order_by(func.random()).limit(length).all()
    return words