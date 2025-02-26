from typing import List, Dict, Iterator, Optional, Union, Any
from data import transactions


def filter_by_currency(list_dict: List[Dict], in_currency: Optional[str] = None) -> Iterator[Union[Dict, str]]:
    """Функция возврата транзакции по заданной валюте"""
    for i in list_dict:
        if in_currency == "":
            raise ValueError("Ошибка: не введена валюта")
        if i["operationAmount"]["currency"]["code"] == in_currency:
            yield i
    else:
        raise ValueError("Ошибка: название валюты не соответствует заданному")


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transaction: List) -> Iterator[Dict[Any, Any]]:
    """Генератор списка возвращающий название операции"""
    for i in transaction:
        for s, w in i.items():
            if s == "description":
                if w == "":
                    raise ValueError("Пустой список: введите название операции")
                yield w
    else:
        raise ValueError("Отсутствует ключ транзакции")


descriptions = transaction_descriptions(transactions)
for _ in range(2):
    print(next(descriptions))


def card_number_generator(start, stop):
    if stop > 9999999999999999:
        raise ValueError("Число превышает допустимый предел")
    elif start <= 0:
        raise ValueError("Число меньше или равно 0")
    elif stop <= start:
        raise ValueError("Несоответствие входных данных")
    else:
        for row in range(start, stop + 1):
            number = "0" * (16 - len(str(row))) + str(row)
            number_card = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
            yield number_card


for card_number in card_number_generator(2, 5):
    print(card_number)
