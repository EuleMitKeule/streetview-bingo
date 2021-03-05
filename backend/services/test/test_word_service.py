from models import Word
import services.word_service as word_service


def test_get_word_by_id(mock_flask_app, mock_word, mock_get_sqlalchemy):

    with mock_flask_app.app_context():
        mock_get_sqlalchemy.filter.return_value.first.return_value = mock_word

        word_id = 1
        response = word_service.get_word(word_id=word_id)

        print(f"id: {response.id}")
        print(f"{response.text}")

        assert response.text == "Stoplight"


def test_create_word(mock_flask_app, mock_db_session, mock_word, mock_get_sqlalchemy):
    
    with mock_flask_app.app_context():
        mock_get_sqlalchemy.filter.return_value.first.return_value = None

        response = word_service.create_word("Bus Stop")

        assert response.text == "Bus Stop"


def test_delete_word(mock_flask_app, mock_db_session, mock_word, mock_get_sqlalchemy):

    with mock_flask_app.app_context():

        mock_get_sqlalchemy.filter.return_value.first.return_value = None
        new_word = word_service.create_word("Dog")

        mock_get_sqlalchemy.filter.return_value.first.return_value = new_word
        word_service.delete_word(word_id=1)

        response = word_service.get_word(word_id=1)
        assert response is None
