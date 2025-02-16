from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data_card_account: str) -> str:
    """Маскировка карты или счета"""
    if data_card_account == "":
        raise ValueError("Введите название объекта")
    number_card = data_card_account.split()[-1]
    name_bill = data_card_account.split()[0]
    if len(number_card) != 16 and len(number_card) != 20:
        raise ValueError("Неверно набрано количество цифр")
    if len(number_card) == 16:
        number_1 = get_mask_card_number(number_card)
        return f"{data_card_account[:-16]} {number_1}"
    elif len(number_card) == 20:
        if name_bill != "Счет":
            raise ValueError("Имя набрано неверно. Повторите попытку")
        number_2 = get_mask_account(number_card)
        return f"{data_card_account[:-20]} {number_2}"
    else:
        return "Введите корректные данные"


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(information: str) -> str:
    """Возврат даты в формате ДД.ММ.ГГГГ"""
    if information == "":
        raise ValueError("Нет данных")
    if len(information) != 26:
        raise ValueError("Ошибка ввода количества знаков")
    if information[4] != "-":
        raise ValueError("Ошибка ввода даты")
    if information[7] != "-":
        raise ValueError("Ошибка ввода даты")
    if information[5:7] > "12":
        raise ValueError("Некорректный ввод месяца")
    if information[8:10] > "31":
        raise ValueError("Некорректный ввод даты")
    if information[0:4] != "2025":
        raise ValueError("Некорректный ввод года")
    data = information[0:10].split("-")
    return ".".join(data[::-1])


print(get_date("2025-12-31T02:26:18.671407"))
