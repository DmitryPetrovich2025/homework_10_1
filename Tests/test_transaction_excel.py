import pandas as pd
from unittest import TestCase
from unittest.mock import patch
from src.transaction_excel import get_reader_transaction_excel


def test_get_reader_transact_excel():          # Отработка ошибки при неправильно указанном пути
    assert get_reader_transaction_excel('transactions') == []


@patch('pandas.read_excel')
def test_get_reader_transaction_excel(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([
        {'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': '23423',
         'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165',
         'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}
    ])

    result = get_reader_transaction_excel('../src/transaction_excel.py')

    assert result == [{'id': '4699552', 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z',
                       'amount': '23423',
                       'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165',
                       'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'
                       }]


class TestCSVFileReader(TestCase):
    @patch('pandas.read_csv', side_effect=FileNotFoundError)
    def test_file_not_found_error(self, mock_read_excel):
        result = get_reader_transaction_excel('non_existent_file.csv')
        self.assertEqual(result, [])
