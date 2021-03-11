from typing import List
from flask import current_app
from models.word import Word
from sqlalchemy.sql.expression import func


db = current_app.db


def get_word(word_id: int = None, text: str = None):
    """
    Returns a word from the word database.

    :param text: The text of the word to return
    :param word_id: The ID of the word to return.
    :returns: The word if found.
    """
    if word_id is not None and text is not None:
        return Word.query.filter(Word.id == word_id).filter(Word.text == text).first()
    elif word_id is not None:
        return Word.query.filter(Word.id == word_id).first()
    elif text is not None:
        return Word.query.filter(Word.text == text).first()
    else:
        return None


def get_words(word_ids: List[int] = None, texts: List[str] = None):
    """
    Returns a list of words from the database

    :param word_ids: The IDs of the words to return
    :param texts: The texts of the words to return
    :returns: A list of words
    """
    words = []

    if word_ids is not None and texts is not None:
        if len(word_ids) != len(texts):
            return None

        for i in range(len(word_ids)):
            word_id = word_ids[i]
            text = texts[i]

            word = get_word(word_id=word_id, text=text)
            if word is not None:
                words.append(word)

        return words

    elif word_ids is not None:
        for word_id in word_ids:
            word = get_word(word_id=word_id)
            if word is not None:
                words.append(word)

        return words

    elif texts is not None:
        for text in texts:
            word = get_word(text=text)
            if word is not None:
                words.append(word)

        return words

    else:
        return None


def get_random_words(length: int):
    """
    Returns a random list of words from the word database.

    :param length: The count of words to return.
    :returns: A list of words.
    """
    words = Word.query.order_by(func.random()).limit(length).all()

    return words


def create_word(text: str):
    """
    Creates a new word in the word database if it doesn't exist yet (case insensitive)

    :param text: The text for the new word
    :returns: The created word if successful
    """
    lower_text = text.lower()
    existing_word = Word.query.filter(func.lower(Word.text) == lower_text).first()

    if existing_word is not None:
        return existing_word

    word = Word(text=text)
    db.session.add(word)

    db.session.commit()
    return word


def delete_word(word_id: int):
    """
    Deletes a word from the word database.

    :param word_id: The ID of the word to delete.
    """
    Word.query.filter(Word.id == word_id).delete()

    db.session.commit()


def delete_words(word_ids: List[int]):
    """
    Deletes words from the word database.

    :param word_ids: The IDs of the words to delete.
    """
    for word_id in word_ids:
        Word.query.filter(Word.id == word_id).delete()

    db.session.commit()
