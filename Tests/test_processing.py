import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_normal_1():  # Проверка при совпадении значения
    assert (filter_by_state([{'id': 41428829, 'state': 'EXECUTED',
                              'date': '2019-07-03T18:35:29.512364'}]) ==
                            [{'id': 41428829, 'state': 'EXECUTED',
                              'date': '2019-07-03T18:35:29.512364'}])


def test_filter_by_state_norma():  # "Проверка при несовпадении значения
    assert filter_by_state([{'id': 41428829, 'state': 'CANCELED',
                             'date': '2019-07-03T18:35:29.512364'}]) == []


def test_filter_by_state_empty_state():  # "Проверка при отсутствии значения
    with pytest.raises(ValueError):
        filter_by_state([{'id': 594226727, 'state': '',
                          'date': '2018-09-12T21:27:25.241689'}])


def test_filter_by_state_invalid_state():  # "Проверка при ошибке ввода значения
    with pytest.raises(ValueError):
        filter_by_state([{'id': 615064591, 'state': 'CANCEL',
                          'date': '2018-10-14T08:21:33.419441'}])


@pytest.fixture
def low_date() -> list:
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-12-12T21:27:25.241689'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-10-12T02:08:58.425572'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T08:21:33.419441'}])


@pytest.fixture
def all_date():
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-10-12T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-12-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T08:21:33.419441'}])


@pytest.fixture
def up_date() -> list:
    return ([{'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T08:21:33.419441'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-10-12T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-12-12T21:27:25.241689'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])


@pytest.fixture
def identical_date_in() -> list:
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-12-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-12-12T08:21:33.419441'}])


@pytest.fixture
def identical_date_out() -> list:
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-12-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-12-12T08:21:33.419441'}])


def test_sort_by_date_low(all_date: list, low_date: list):
    # Проверка обработки в порядке убывания по дате
    assert sort_by_date(all_date) == low_date


def test_sort_by_date_up(all_date: list, up_date: list):
    # Проверка обработки в порядке возрастания по дате
    assert sort_by_date(all_date, sort_key=False) == up_date


def test_sort_by_date_identical(identical_date_in: list, identical_date_out: list):
    # Проверка обработки при наличии одинаковых дат
    assert sort_by_date(identical_date_in) == identical_date_out


def test_sort_by_date_empty():
    # Проверка обработки при отсутствии даты
    with pytest.raises(ValueError):
        sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': ''}])


def test_sort_by_date_invalid_date():
    # Проверка обработки при некорректном вводе количества знаков в дате
    with pytest.raises(ValueError):
        sort_by_date([{'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12'}])
