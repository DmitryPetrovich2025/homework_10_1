import pandas as pd
from unittest import TestCase
from unittest.mock import patch
from src.transaction_csv import get_reader_transaction_csv


def test_get_reader_transaction_csv():          # Отработка ошибки при неправильно указанном пути
    assert get_reader_transaction_csv('./data/transactions') == []


@patch('pandas.read_csv')  # Проверка работы функции
def test_get_reader_transaction_excel(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame([
        {'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': '23423',
         'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165',
         'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}
    ])

    result = get_reader_transaction_csv('../src/transaction_csv.py')

    assert result == [{'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z',
                       'amount': '23423',
                       'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165',
                       'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'
                       }]


class TestCSVFileReader(TestCase):  # Обработка ошибки, когда файл не найден или неверно указан путь
    @patch('pandas.read_csv', side_effect=FileNotFoundError)
    def test_file_not_found_error(self, mock_read_csv):
        result = get_reader_transaction_csv('non_existent_file.csv')
        self.assertEqual(result, [])
