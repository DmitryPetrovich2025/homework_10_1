import pytest
from src.generators import filter_by_currency
from data.date import transactions, transactions_output_1, transactions_output_2


def test_filter_by_currency_invalid_empty_list():  # Пустой список выбора валюты
    with pytest.raises(ValueError):
        for list_transaction in filter_by_currency(transactions, ""):
            print(list_transaction)


def test_filter_by_currency_invalid_input():       # Ошибка ввода названия валюты
    with pytest.raises(ValueError):
        for list_transaction in filter_by_currency(transactions, "US"):
            print(list_transaction)


def test_filter_by_currency_normal_work():         # Проверка работы фильтра
    gen = filter_by_currency(transactions, "USD")
    assert next(gen) == transactions_output_1
    assert next(gen) == transactions_output_2
