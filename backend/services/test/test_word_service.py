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