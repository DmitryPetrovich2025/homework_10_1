import pytest
from data import transactions_invalid, transactions, transactions_invalid_2
from src.generators import transaction_descriptions


def test_transaction_descriptions_invalid():       # Пустой список транзакции
    with pytest.raises(ValueError):
        for list_transaction in transaction_descriptions(transactions_invalid):
            print(list_transaction)


def test_transaction_descriptions_normal_work():   # Проверка работы генератора
    gen = transaction_descriptions(transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"


def test_transaction_descriptions_invalid_description():  # Ошибка отсутствия ключа транзакции
    with pytest.raises(ValueError):
        for list_transaction in transaction_descriptions(transactions_invalid_2):
            print(list_transaction)
