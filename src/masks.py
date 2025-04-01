import logging


logger = logging.getLogger("masks")
file_handler = logging.FileHandler("masks.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера карты"""
    logger.info("Начало работы программы маскировки номера карты.")
    if len(number_card) == 0:
        error_message = "Номер карты не набран"
        logger.error(error_message)
        raise ValueError(error_message)
    if len(number_card) > 16 or len(number_card) < 16:
        error_message = "Ошибка в количестве цифр"
        logger.error(error_message)
        raise ValueError(error_message)
    if not number_card.isdigit():
        error_message = "Введены не только цифры"
        logger.error(error_message)
        raise ValueError(error_message)
    if len(number_card) == 16:
        logger.info("Процесс маскировки карты. Окончание работы программы.")
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
    else:
        error_message = "Неверно набран номер карты. Повторите попытку."
        logger.error(error_message)
        return error_message


def get_mask_account(number_account: str) -> str:
    """Функция маскировки номера счёта"""
    logger.info("Начало работы программы маскировки номера счёта.")
    if len(number_account) > 20:
        error_message = "Количество цифр больше 20"
        logger.error(error_message)
        raise ValueError(error_message)
    if len(number_account) < 20:
        error_message = "Количество цифр меньше 20"
        logger.error(error_message)
        raise ValueError(error_message)
    if not number_account.isdigit():
        error_message = "Ошибка ввода: введены не только цифры"
        logger.error(error_message)
        raise ValueError(error_message)
    if len(number_account) == 20 and number_account.isdigit():
        logger.info("Процесс маскировки номера счёта. Окончание работы программы.")
        return f"**{number_account[-4:]}"
    else:
        error_message = "Неверно набран номер счета. Повторите попытку."
        logger.error(error_message)
        return error_message


print(get_mask_card_number("3452345673454345"))
print(get_mask_account("35246372837362534362"))
