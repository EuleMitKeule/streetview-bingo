

def test_get_word_by_id(mock_flask_app):

    with mock_flask_app.app_context():
        import services.word_service as word_service
        from models.word import Word
        from flask import current_app

        db = current_app.db
        db.drop_all()
        db.session.commit()

        db.create_all()
        db.session.commit()

        test_word = Word(text="Stoplight")

        db.session.add(test_word)
        db.session.commit()

        word_id = 1
        response = word_service.get_word(word_id=word_id)

        print(f"id: {response.id}")
        print(f"{response.text}")

        assert response.text == "Stoplight"


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

#
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
