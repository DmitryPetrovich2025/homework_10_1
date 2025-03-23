import json
import logging


logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_to_transaction_file(path_to_file: str) -> list:
    """Функция принимает на вход путь до JSON-файла
       и возвращает список словарей о транзакциях   """
    logger.info("Начало работы программы по обработке JSON-файла.")
    try:
        with open(path_to_file, "r", encoding="Utf8") as file:
            try:
                logger.info("Процесс обработки JSON-файла.")
                data_transactions = json.load(file)
                logger.info("Окончание работы программы, возврат списка словарей о транзакциях.")
                return data_transactions
            except json.JSONDecodeError:
                logger.error("Ошибка в преобразовании JSON-файла.Необходимо проверить формат файла.")
                data_transactions = []
                return data_transactions
    except FileNotFoundError:
        logger.error("Файл не был найден, необходимо скорректировать или проверить путь.")
        data_transactions = []
        return data_transactions


if __name__ == "__main__":
    print(get_to_transaction_file("../data/operations.json"))
