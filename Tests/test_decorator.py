import pytest
from src.decorators import my_function


def test_my_function_type_error():         # Проверка выброса ошибки при
    with pytest.raises(TypeError):         # некорректно введенном параметре
        my_function(4, "e")          # при выводе результата в mylog.txt


def test_my_function_positive():            # Проверка правильности обработки
    positive = my_function(4, 2)      # данных при корректных входных данных
    assert positive == 2.0


def test_my_function_log(capsys):            # Проверка вывода в консоль при
    my_function(0, 3)                  # записи в файл mylog.txt
    captured = capsys.readouterr()
    assert "" in captured.out


def test_my_function_zero_invalid():         # Проверка выброса ошибки
    with pytest.raises(ZeroDivisionError):   # при делении на "0"
        my_function(2, 0)


def test_result_my_function_in_file():       # Проверка логирования
    my_function(2, 4)                  # результата в файл
    with open("mylog.txt", "r", encoding="utf-8") as file:
        logs = file.readlines()
        assert "my_function ok\n" in logs[-1]
