import pandas as pd


def get_reader_transaction_excel(file_excel: str) -> list:
    """Считывание транзакции из XLSX-файла и возврат списка словарей"""
    try:
        df = pd.read_excel(file_excel, dtype=str, engine='openpyxl')
        transaction_excel = df.to_dict(orient='records')
        return transaction_excel
    except FileNotFoundError:
       # print('Ошибка: файл не найден.')
        return []
    except UnicodeDecodeError:
        print('Ошибка в кодировке файла')
        return []


if __name__ == '__main__':
    result = get_reader_transaction_excel('../data/transactions_excel.xlsx')
    print(result)
