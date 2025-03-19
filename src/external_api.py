import os
import requests
from typing import Any
from requests import RequestException
from dotenv import load_dotenv
from data.normal_date import operation_normal_out


load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")


def transaction_amount_in_rub(transactions: list, transaction_id: int) -> Any:
    """Обработка транзакций и вывод суммы в рублях с конвертацией, если данные в валюте"""
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            try:
                if transaction["operationAmount"]["currency"]["code"] == "RUB":
                    amount_rub = transaction["operationAmount"]["amount"]
                    if amount_rub == "0" or amount_rub == "":
                        raise ValueError("Ошибка в отсутствии или некорректности значения ")
                    return float(amount_rub)
                elif transaction["operationAmount"]["currency"]["code"] == "USD":
                    amount_usd = transaction["operationAmount"]["amount"]
                    if amount_usd == "0" or amount_usd == "":
                        raise ValueError("Ошибка в отсутствии или некорректности значения ")
                    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount_usd}"
                    headers = {"apikey": API_KEY}
                    response = requests.get(url, headers=headers)
                    json_result = response.json()
                    usd_to_rub_amount = json_result["result"]
                    return float(usd_to_rub_amount)
                elif transaction["operationAmount"]["currency"]["code"] == "EUR":
                    amount_eur = transaction["operationAmount"]["amount"]
                    if amount_eur == "0" or amount_eur == "":
                        raise ValueError("Ошибка в отсутствии или некорректности значения ")
                    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount_eur}"
                    headers = {"apikey": API_KEY}
                    response = requests.get(url, headers=headers)
                    json_result = response.json()
                    eur_to_rub_amount = json_result["result"]
                    return float(eur_to_rub_amount)
            except RequestException:
                return "Ошибка связи, корректности запроса"


if __name__ == "__main__":
    print(transaction_amount_in_rub(transactions=operation_normal_out, transaction_id=441945886))
