import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("number_card, expected",
                         [("7000792289606361", "7000 79** **** 6361"),
                          ("8000499682897642", "8000 49** **** 7642"),
                          ("4000646578562624", "4000 64** **** 2624")])
def test_get_mask_card_number_normal(number_card: str, expected: str):  # Проверка правильности
    assert get_mask_card_number(number_card) == expected                # обработки номера карты


def test_get_mask_card_number_small_number(): # Проверка при наборе меньшего количества цифр
    with pytest.raises(ValueError):
        get_mask_card_number("700079228960636")


def test_get_mask_card_number_more_number():    # Проверка при наборе цифр больше 16
    with pytest.raises(ValueError):
        get_mask_card_number("700079228960636123")


def test_get_mask_card_number_invalid_number(): # Проверка при ошибке набора номера кроме цифр
    with pytest.raises(ValueError):
        get_mask_card_number("700079d2896063r")


@pytest.mark.parametrize("number_account, expected",
                         [("70007922896063612314", "**2314"),
                          ("80004996828976422356", "**2356"),
                          ("40006465785626244578", "**4578")])
def test_get_mask_account_normal(number_account: str, expected: str):  # Проверка правильности
    assert get_mask_account(number_account) == expected                # обработки счета


def test_get_mask_account_more():    # Проверка при наборе счета больше 20 цифр
    with pytest.raises(ValueError):
        get_mask_account("700079289606335678532")


def test_get_mask_account_minimum():  # Проверка при наборе счета меньше 20 цифр
    with pytest.raises(ValueError):
        get_mask_account("700079289678")


def test_get_mask_account_invalid():  # Проверка при наборе букв
    with pytest.raises(ValueError):
        get_mask_account("700024S789346T68904e")
