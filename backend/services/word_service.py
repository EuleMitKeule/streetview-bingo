from config import db
from models import Word
from sqlalchemy.sql.expression import func


def get_random_words(length: int):
    """
        Returns a random list of words from the word database.

        Parameters:
            length(int): The count of words to return.
        Returns:
            A list of words.
    """
    words = Word.query.order_by(func.random()).limit(length).all()
    return words


def get_word(word_id: int):
    """
        Returns a word from the word database.

        Parameters:
            word_id(int): The ID of the word to return.
        Returns:
            The word if it was found.
    """
    word = Word.query.filter(Word.id == word_id).first()
    return word


def get_words(word_ids: list[int]):
    """
        Returns a list of words from the database

        Parameters:
             word_ids(list[int]): The IDs of the words to return
         Returns:
             A list of words
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

        Parameters:
            word_id(int): The ID of the word to delete.
    """
    Word.query.filter(Word.id == word_id).first().delete()


def delete_words(word_ids: list[int]):
    """
        Deletes words from the word database.

        Parameters:
             word_ids(list[int]): The IDs of the words to delete.
    """
    for word_id in word_ids:
        Word.query.filter(Word.id == word_id).first().delete()


def create_word(text: str):
    """
        Creates a new word in the word database if it doesn't exist yet (case insensitive)

        Parameters:
            text(str): The text for the new word
        Returns:
            The created word if successful
    """
    lower_text = text.lower()
    existing_word = Word.query.filter(Word.text.lower() == lower_text).first()

    if existing_word is not None:
        return None

    word = Word(text=text)
    db.session.add(word)

    db.session.commit()

    return word
