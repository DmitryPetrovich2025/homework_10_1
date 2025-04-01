import pandas as pd


def get_reader_transaction_csv(file_csv: str) -> list:
    """Считывание транзакции из CSV-файла и возврат списка словарей"""
    try:
        df = pd.read_csv(file_csv, dtype=str, delimiter=';')
        transaction_csv = df.to_dict(orient='records')
        return transaction_csv
    except FileNotFoundError:
        print('Ошибка: файл не найден.')
        return []
    except UnicodeDecodeError:
        print('Ошибка в кодировке файла.')
        return []


if __name__ == '__main__':
    result = get_reader_transaction_csv('../data/transactions.csv')
    print(result)
