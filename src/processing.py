from typing import List, Dict


def filter_by_state(handling_data: List[Dict], state: str = "EXECUTED") -> List:
    """Функция обработки данных с возвратом списка по значению"""
    new_list = []
    for i in handling_data:
        if i.get("state") == "":
            raise ValueError("Значение не обозначено")
        if i.get("state") != "EXECUTED" and i.get("state") != "CANCELED":
            raise ValueError("Значение неправильно введено")
        if i.get("state") == state:
            new_list.append(i)
    return new_list


print(filter_by_state([
    {'id':  41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]))


print(filter_by_state([
     {'id':  41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
      state="CANCELED"))


def sort_by_date(date_info: List[Dict], sort_key: bool = True) -> List[Dict]:
    """Функция сортировки данных по дате"""
    for i in date_info:
        if i.get("date") == "":
            raise ValueError("Дата не введена")
        if len(i.get("date")) != 26:
            raise ValueError("Ошибка в количестве данных")
    return sorted(date_info, key=lambda x: x["date"], reverse=sort_key)


print(sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-12-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-10-12T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-12-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T08:21:33.419441'}
], sort_key=False))


print(sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-10-12T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-12-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T08:21:33.419441'}
]))


print(sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-12-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-12-12T08:21:33.419441'}
]))
