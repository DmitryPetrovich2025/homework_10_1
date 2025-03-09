import pytest
from src.generators import card_number_generator


def test_card_number_generator_more_number():            # Число "stop" больше 16 знаков
    with pytest.raises(ValueError):
        for card_number in card_number_generator(2, 57777777777777777777):
            print(card_number)


def test_card_number_generator_invalid_for_zero_start():  # Число "start" меньше 0
    with pytest.raises(ValueError):
        for card_number in card_number_generator(0, 5):
            print(card_number)


def test_card_number_generator_invalid_start():            # Число "stop" меньше "start"
    with pytest.raises(ValueError):
        for card_number in card_number_generator(55, 45):
            print(card_number)


def test_card_number_generator_normal_date():              # Проверка работы генератора
    gen = card_number_generator(2, 5)
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    assert next(gen) == "0000 0000 0000 0004"
    assert next(gen) == "0000 0000 0000 0005"
