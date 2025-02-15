def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера карты"""

    if len(number_card) > 16 or len(number_card) < 16:
        raise ValueError("Ошибка в количестве цифр")
    if not number_card.isdigit():
        raise ValueError("Введены не только цифры")
    if len(number_card) == 16 and number_card.isdigit():
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
    else:
        return "Неверно набран номер карты. Повторите попытку."


def get_mask_account(number_account: str) -> str:
    """Функция маскировки номера счёта"""
    if len(number_account) > 20:
        raise ValueError("Количество цифр больше 20")
    if len(number_account) < 20:
        raise ValueError("Количество цифр меньше 20")
    if not number_account.isdigit():
        raise ValueError("Ошибка ввода: введены не только цифры")
    if len(number_account) == 20 and number_account.isdigit():
        return f"**{number_account[-4:]}"
    else:
        return "Неверно набран номер счета. Повторите попытку."


print(get_mask_card_number("7000792289606364"))
print(get_mask_account("73654108430135874303"))
