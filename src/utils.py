import json


def get_to_transaction_file(path_to_file: str) -> list:
    """Функция принимает на вход путь до JSON-файла
       и возвращает список словарей о транзакциях   """
    try:
        with open(path_to_file, "r", encoding="Utf8") as file:
            try:
                data_transactions = json.load(file)
                return data_transactions
            except json.JSONDecodeError:
                data_transactions = []
                return data_transactions
    except FileNotFoundError:
        data_transactions = []
        return data_transactions


if __name__ == "__main__":
    print(get_to_transaction_file("../data/operations.json"))
