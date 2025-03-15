from src.utils import get_to_transaction_file
from data.normal_date import operation_normal_out


def test_get_to_transaction_file_empty_list():
    """Проверка работы программы при пустом списке"""
    assert (get_to_transaction_file("C:/Users/DK/PycharmProjects/PythonProject/"
                                    "PythonProject/Project_homework_10_1/data/"
                                    "operations_empty.json")) == []


def test_get_to_transaction_file_no_list():
    """Проверка работы программы если входные данные не список"""
    assert (get_to_transaction_file("C:/Users/DK/PycharmProjects/PythonProject/"
                                    "PythonProject/Project_homework_10_1/data/"
                                    "operations_no_list.json")) == []


def test_get_to_transaction_file_normal():
    """Проверка корректности обработки данных"""
    positive = get_to_transaction_file("C:/Users/DK/PycharmProjects/PythonProject/"
                                       "PythonProject/Project_homework_10_1/data/"
                                       "operations.json")
    assert positive == operation_normal_out


def test_get_to_transaction_file_invalid_json():
    """Проверка работы программы при некорректном json файле"""
    assert (get_to_transaction_file("C:/Users/DK/PycharmProjects/PythonProject/"
                                    "PythonProject/Project_homework_10_1/data/"
                                    "operations_invalid.json")) == []
