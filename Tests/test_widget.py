import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("data_card_account, expected",
                         [("Maestro 1596837868705199", "Maestro  1596 83** **** 5199"),
                          ("Mastercard 7158300734726758", "Mastercard  7158 30** **** 6758"),
                          ("Счет 64686473678894779589", "Счет  **9589")])  # Проверка правильности
def test_mask_account_card_normal(data_card_account: str, expected: str):  # обработки данных
    assert mask_account_card(data_card_account) == expected


def test_mask_account_card_empty_list():      # Проверка пустого списка
    with pytest.raises(ValueError):
        mask_account_card("")


def test_mask_account_card_number_invalid():   # Проверка на корректное количество цифр
    with pytest.raises(ValueError):
        mask_account_card("234456782345")


def test_mask_account_card_name_invalid():     # Проверка на корректное имя
    with pytest.raises(ValueError):
        mask_account_card("Сч")


@pytest.mark.parametrize("inform, expected",  # Проверка корректности обработки данных
                         [("2024-03-11T02:26:18.671407", "11.03.2024"),
                          ("2024-04-30T02:26:18.671407", "30.04.2024"),
                          ("2024-12-31T02:26:18.671407", "31.12.2024")])
def test_get_date_normal(inform: str, expected: str):
    assert get_date(inform) == expected


def test_get_date_empty_list():     # Проверка отработки при пустом списке
    with pytest.raises(ValueError):
        get_date("")


def test_get_date_invalid_information():       # Проверка обработки при
    with pytest.raises(ValueError):            # ошибке в количестве знаков
        get_date("2024-03-T02:26:18.671407")


def test_get_date_invalid_data():               # Проверка обработки при
    with pytest.raises(ValueError):             # ошибке ввода даты
        get_date("2024/03-31T02:26:18.671407")


def test_get_date_invalid_data_1():             # Проверка обработки при
    with pytest.raises(ValueError):             # ошибке ввода даты
        get_date("2024-03&31T02:26:18.671407")


def test_get_date_invalid_month():              # Проверка обработки при
    with pytest.raises(ValueError):             # ошибке ввода месяца
        get_date("2024-16-12T02:26:18.671407")


def test_get_date_invalid_date():               # Проверка обработки при
    with pytest.raises(ValueError):             # ошибке ввода даты
        get_date("2024-12-32T02:26:18.671407")


def test_get_date_invalid_year():               # Проверка обработки при
    with pytest.raises(ValueError):             # ошибке ввода года
        get_date("2022-12-31T02:26:18.671407")
