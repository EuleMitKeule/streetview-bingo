

def test_get_word_by_id(mock_streetview_bingo):
    import services.word_service as word_service

    new_word = word_service.create_word(text="Stoplight")

    response = word_service.get_word(word_id=new_word.id)

    assert response.text == "Stoplight"

    response = word_service.get_word(word_id=-1)

    assert response is None


def test_get_word_by_text(mock_streetview_bingo):
    import services.word_service as word_service

    new_word = word_service.create_word(text="Person Smoking")

    response = word_service.get_word(text=new_word.text)

    assert response.text == "Person Smoking"

    response = word_service.get_word(text="Non-Smoker")

    assert response is None


def test_get_word_by_id_and_text(mock_streetview_bingo):
    import services.word_service as word_service

    first_word = word_service.create_word(text="Hanging Bridge")
    second_word = word_service.create_word(text="Suspension Bridge")

    result = word_service.get_word(word_id=second_word.id, text=second_word.text)

    assert result.id == second_word.id and result.text == second_word.text

    result = word_service.get_word(word_id=first_word.id, text=second_word.text)

    assert result is None


def test_get_word_by_none(mock_streetview_bingo):
    import services.word_service as word_service

    word_service.create_word(text="Waterfall")

    response = word_service.get_word()

    assert response is None


def test_get_words_by_ids(mock_streetview_bingo):
    import services.word_service as word_service

    first_word = word_service.create_word(text="UPS Truck")
    second_word = word_service.create_word(text="DPD Truck")
    third_word = word_service.create_word(text="DHL Truck")

    word_ids = [first_word.id, third_word.id]
    result = word_service.get_words(word_ids)

    assert result[0].text == first_word.text and result[1].text == third_word.text

    word_ids = [second_word.id, third_word.id + 1]
    result = word_service.get_words(word_ids)

    assert result[0].text == second_word.text and len(result) == 1

    word_ids = [third_word.id + 1, third_word.id + 2, third_word.id + 3]
    result = word_service.get_words(word_ids)

    assert len(result) == 0

    word_service.create_word("DHL Truck")

    word_ids = [third_word.id]
    result = word_service.get_words(word_ids)

    assert len(result) == 1

    result = word_service.get_words(word_ids=[])

    assert len(result) == 0


def test_get_words_by_texts(mock_streetview_bingo):
    import services.word_service as word_service

    first_word = word_service.create_word(text="NA Miata")
    second_word = word_service.create_word(text="NB Miata")
    third_word = word_service.create_word(text="NC Miata")
    word_service.create_word(text="ND Miata")

    texts = [first_word.text, third_word.text]
    result = word_service.get_words(texts=texts)

    assert result[0].id == first_word.id and result[1].text == third_word.text and len(result) == 2

    texts = [second_word.text, "NE Miata"]
    result = word_service.get_words(texts=texts)

    assert result[0].text == second_word.text and len(result) == 1

    texts = ["Honda 2000"]
    result = word_service.get_words(texts=texts)

    assert len(result) == 0


def test_get_words_by_ids_and_texts(mock_streetview_bingo):
    import services.word_service as word_service

    first_word = word_service.create_word(text="test 1")
    second_word = word_service.create_word(text="test 2")
    third_word = word_service.create_word(text="test 3")

    word_ids = [first_word.id, third_word.id]
    texts = [first_word.text, third_word.text]
    result = word_service.get_words(word_ids=word_ids, texts=texts)

    assert result[0].text == first_word.text and result[1].id == third_word.id and len(result) == 2

    word_ids = [first_word.id, third_word.id + 1]
    texts = [first_word.text, third_word.text]
    result = word_service.get_words(word_ids=word_ids, texts=texts)

    assert result[0].text == first_word.text and len(result) == 1

    word_ids = [first_word.id]
    texts = [first_word.text, second_word.text]
    result = word_service.get_words(word_ids=word_ids, texts=texts)

    assert result is None


def test_get_words_by_none(mock_streetview_bingo):
    import services.word_service as word_service

    word_service.create_word(text="test")

    result = word_service.get_words()

    assert result is None


def test_get_random_words(mock_streetview_bingo):
    import services.word_service as word_service

    word_service.create_word(text="Some")
    word_service.create_word(text="Thing")
    word_service.create_word(text="Something")

    results = word_service.get_random_words(length=2)

    assert len(results) == 2
    assert results[0] != results[1]


def test_create_word(mock_streetview_bingo):
    import services.word_service as word_service

    new_word = word_service.create_word("Cat")

    assert new_word.text == "Cat"

    result = word_service.get_word(new_word.id)

    assert result.text == "Cat"


def test_create_empty(mock_streetview_bingo):
    import services.word_service as word_service

    new_word = word_service.create_word(" ** $0123 .-,")

    assert new_word is None


def test_create_word_duplicate(mock_streetview_bingo):
    import services.word_service as word_service
    from models.word import Word

    word_service.create_word("Fox")
    new_word = word_service.create_word("Fox")

    assert new_word.text == "Fox"

    result = Word.query.filter(Word.text == "Fox").all()

    assert len(result) == 1


def test_delete_word(mock_streetview_bingo):
    import services.word_service as word_service

    new_word = word_service.create_word("Bulldog")

    result = word_service.get_word(word_id=new_word.id)

    assert result is not None

    word_service.delete_word(word_id=new_word.id)

    result = word_service.get_word(word_id=new_word.id)

    assert result is None


def test_delete_words(mock_streetview_bingo):
    import services.word_service as word_service

    first_word = word_service.create_word("Dog")
    second_word = word_service.create_word("Stoplight")

    word_ids = [first_word.id, second_word.id]
    word_service.delete_words(word_ids=word_ids)

    response = word_service.get_words(word_ids=word_ids)

    assert len(response) == 0
