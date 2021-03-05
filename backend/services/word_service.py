from typing import List
from flask import current_app
from models import Word
from sqlalchemy.sql.expression import func


db = current_app.db


def get_word(word_id: int = None, text: str = None):
    """
    Returns a word from the word database.

    :param text: The text of the word to return
    :param word_id: The ID of the word to return.
    :returns: The word if found.
    """
    if word_id is not None:
        return Word.query.filter(Word.id == word_id).first()
    elif text is not None:
        return Word.query.filter(Word.text == text).first()
    else:
        return None


def get_words(word_ids: List[int]):
    """
    Returns a list of words from the database

    :param word_ids: The IDs of the words to return
    :returns: A list of words
    """
    words = []

    for word_id in word_ids:
        word = get_word(word_id=word_id)
        if word is not None:
            words.append(word)

    return words


def get_random_words(length: int):
    """
    Returns a random list of words from the word database.

    :param length: The count of words to return.
    :returns: A list of words.
    """
    words = Word.query.order_by(func.random()).limit(length).all()

    return words


def delete_word(word_id: int):
    """
    Deletes a word from the word database.

    :param word_id: The ID of the word to delete.
    """
    Word.query.filter(Word.id == word_id).first().delete()

    db.session.commit()


def delete_words(word_ids: List[int]):
    """
    Deletes words from the word database.

    :param word_ids: The IDs of the words to delete.
    """
    for word_id in word_ids:
        Word.query.filter(Word.id == word_id).first().delete()

    db.session.commit()


def create_word(text: str):
    """
    Creates a new word in the word database if it doesn't exist yet (case insensitive)

    :param text: The text for the new word
    :returns: The created word if successful
    """
    lower_text = text.lower()
    existing_word = Word.query.filter(str(Word.text).lower() == lower_text).first()

    if existing_word is not None:
        return None

    word = Word(text=text)
    db.session.add(word)

    db.session.commit()
    return word
