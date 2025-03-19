import pytest
from unittest.mock import patch
from src.external_api import transaction_amount_in_rub, API_KEY
from data.normal_date import operation_normal_out


def test_transaction_amount_in_rub_invalid_empty():
    """Проверка при отсутствии значения"""
    with pytest.raises(ValueError):
        transaction_amount_in_rub([
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                }}], 441945886)


def test_transaction_amount_in_rub_invalid_correct_date():
    """Проверка при некорректном значении"""
    with pytest.raises(ValueError):
        transaction_amount_in_rub([
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "34er",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                }}], 441945886)


def test_transaction_amount_in_rub_invalid_date_usd():
    """Проверка при отсутствии значении USD"""
    with pytest.raises(ValueError):
        transaction_amount_in_rub([
            {
                 "id": 41428829,
                 "state": "EXECUTED",
                 "date": "2019-07-03T18:35:29.512364",
                 "operationAmount": {
                     "amount": "",
                     "currency": {
                         "name": "USD",
                         "code": "USD"
                     }
                 }}], 41428829)


def test_transaction_amount_in_rub_invalid_date_eur():
    """Проверка при нулевом значении EUR"""
    with pytest.raises(ValueError):
        transaction_amount_in_rub([
            {
                 "id": 41428829,
                 "state": "EXECUTED",
                 "date": "2019-07-03T18:35:29.512364",
                 "operationAmount": {
                     "amount": "0",
                     "currency": {
                         "name": "EUR",
                         "code": "EUR"
                     }
                 }}], 41428829)


def test_transaction_amount_in_rub_normal_result():
    """Тестирование возврата значения при транзакции в рублях"""
    result = transaction_amount_in_rub([
      {
          "id": 441945886,
          "state": "EXECUTED",
          "date": "2019-08-26T10:50:58.294041",
          "operationAmount": {
              "amount": "34516.67",
              "currency": {
                "name": "руб.",
                "code": "RUB"
              }
          }}], 441945886)
    assert result == 34516.67


@patch("requests.get")
def test_transaction_amount_eur_in_rub(mock_get):
    """Тестирование возврата значения при транзакции в евро"""
    expected = {'success': True, 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 79114.93},
                'info': {'timestamp': 1742339763, 'rate': 89.45471}, 'date': '2025-03-18',
                'result': 7077203.11982}
    mock_get.return_value.json.return_value = expected
    assert transaction_amount_in_rub(transactions=operation_normal_out, transaction_id=142264268) == expected["result"]
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/"
                                     "convert?to=RUB&from=EUR&amount=79114.93",
                                     headers={'apikey': API_KEY})


@patch("requests.get")
def test_transaction_amount_usd_in_rub(mock_get):
    """Тестирование возврата значения при транзакции в долларах"""
    expected = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 9824.07},
                'info': {'timestamp': 1742340964, 'rate': 81.749629}, 'date': '2025-03-18',
                'result': 803114.07777}
    mock_get.return_value.json.return_value = expected
    assert transaction_amount_in_rub(transactions=operation_normal_out, transaction_id=939719570) == expected["result"]
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/"
                                     "convert?to=RUB&from=USD&amount=9824.07",
                                     headers={'apikey': API_KEY})
