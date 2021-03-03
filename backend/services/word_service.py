from config import db
from models import Word
from sqlalchemy.sql.expression import func


def get_random_words(length: int):
    """
        Returns a random list of words from the word database.

        :param length: The count of words to return.
        :returns: A list of words.
    """
    words = Word.query.order_by(func.random()).limit(length).all()
    return words


def get_word(word_id: int):
    """
        Returns a word from the word database.

        :param word_id: The ID of the word to return.
        :returns: The word if it was found.
    """
    word = Word.query.filter(Word.id == word_id).first()
    return word


def get_words(word_ids: list[int]):
    """
        Returns a list of words from the database

        :param word_ids: The IDs of the words to return
        :returns: A list of words
    """
    words = []

    for word_id in word_ids:
        word = Word.query.filter(Word.id == word_id).first()
        if word is not None:
            words.append(word)

    return words


def delete_word(word_id: int):
    """
        Deletes a word from the word database.

        :param word_id: The ID of the word to delete.
    """
    Word.query.filter(Word.id == word_id).first().delete()


def delete_words(word_ids: list[int]):
    """
        Deletes words from the word database.

        :param word_ids: The IDs of the words to delete.
    """
    for word_id in word_ids:
        Word.query.filter(Word.id == word_id).first().delete()


def create_word(text: str):
    """
        Creates a new word in the word database if it doesn't exist yet (case insensitive)

        :param text: The text for the new word
        :returns: The created word if successful
    """
    lower_text = text.lower()
    existing_word = Word.query.filter(Word.text.lower() == lower_text).first()

    if existing_word is not None:
        return None

    word = Word(text=text)
    db.session.add(word)

    db.session.commit()

    return word
