def test_get_word_by_id_and_text(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db

        Word.query.delete()
        db.session.commit()

        word_service.create_word(text="Hanging Bridge")
        word_service.create_word(text="Suspension Bridge")

        result = word_service.get_word(word_id=2, text="Suspension Bridge")

        assert result.id == 2 and result.text == "Suspension Bridge"

        result = word_service.get_word(word_id=1, text="Suspension Bridge")

        assert result is None


def test_get_word_by_id(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db

        Word.query.delete()
        db.session.commit()

        db.create_all()

        word_service.create_word(text="Stoplight")

        word_id = 1
        response = word_service.get_word(word_id=word_id)

        assert response.text == "Stoplight"

        word_id = 2
        response = word_service.get_word(word_id=word_id)

        assert response is None

        db.session.close()


def test_get_word_by_text(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db

        Word.query.delete()
        db.session.commit()

        word_text = "Person Smoking"
        word_service.create_word(text=word_text)

        response = word_service.get_word(text=word_text)

        assert response.text == word_text

        response = word_service.get_word(text="Non-Smoker")

        assert response is None


def test_get_word_by_none(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db

        Word.query.delete()
        db.session.commit()

        word_service.create_word(text="Waterfall")

        response = word_service.get_word()

        assert response is None


def test_get_words_by_ids_and_texts(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db

        Word.query.delete()
        db.session.commit()

        word_service.create_word(text="test 1")
        word_service.create_word(text="test 2")
        word_service.create_word(text="test 3")

        word_ids = [1, 3]
        texts = ["test 1", "test 3"]
        result = word_service.get_words(word_ids=word_ids, texts=texts)

        assert result[0].text == "test 1" and result[1].id == 3 and len(result) == 2

        word_ids = [1, 4]
        result = word_service.get_words(word_ids=word_ids, texts=texts)

        assert result[0].text == "test 1" and len(result) == 1

        word_service.create_word(text="test 1")

        texts = ["test 1", "test 1"]
        result = word_service.get_words(word_ids=word_ids, texts=texts)

        assert result[0].text == "test 1" and result[1].id == 4 and len(result) == 2


def test_get_words_by_ids(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db

        Word.query.delete()
        db.session.commit()

        word_service.create_word(text="UPS Truck")
        word_service.create_word(text="DPD Truck")
        word_service.create_word(text="DHL Truck")

        word_ids = [1, 3]
        result = word_service.get_words(word_ids)

        assert result[0].text == "UPS Truck" and result[1].text == "DHL Truck"

        word_ids = [2, 4]
        result = word_service.get_words(word_ids)

        assert result[0].text == "DPD Truck" and len(result) == 1

        word_ids = [4, 5, 6]
        result = word_service.get_words(word_ids)

        assert len(result) == 0

        word_service.create_word("DHL Truck")

        word_ids = [3]
        result = word_service.get_words(word_ids)

        assert len(result) == 1

        result = word_service.get_words()

        assert result is None


def test_get_words_by_texts(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db

        Word.query.delete()
        db.session.commit()

        word_service.create_word(text="NA Miata")
        word_service.create_word(text="NB Miata")
        word_service.create_word(text="NC Miata")
        word_service.create_word(text="ND Miata")

        texts = ["NA Miata", "NC Miata"]
        result = word_service.get_words(texts=texts)

        assert result[0].id == 1 and result[1].text == "NC Miata" and len(result) == 2

        texts = ["NB Miata", "NE Miata"]
        result = word_service.get_words(texts=texts)

        assert result[0].text == "NB Miata" and len(result) == 1

        texts = ["Honda 2000"]
        result = word_service.get_words(texts=texts)

        assert len(result) == 0


def test_create_word(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db

        Word.query.delete()
        db.session.commit()

        db.create_all()

        new_word = word_service.create_word("Bus Stop")

        assert new_word.id == 1
        assert new_word.text == "Bus Stop"

        result = Word.query.filter(Word.id == new_word.id and Word.text == new_word.text).first()

        assert result.id == 1
        assert result.text == "Bus Stop"


def test_get_words_by_none(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db

        Word.query.delete()
        db.session.commit()

        word_service.create_word(text="test")

        result = word_service.get_words()

        assert result is None


# def test_delete_word(mock_flask_app):
#
#     with mock_flask_app.app_context():
#         import services.word_service as word_service
#         from models.word import Word
#         from flask import current_app
#
#         new_word = word_service.create_word("Dog")
#
#         word_service.delete_word(word_id=1)
#         response = word_service.get_word(word_id=1)
#
#         assert response is None
