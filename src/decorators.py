from collections.abc import Callable
from typing import Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, принимающий аргумент "filename" и записывающий
    логи в файл(filename задан) или выводящий лог в консоль
    (filename не задан).
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    error_type = type(e).__name__
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error_type}. Inputs {args}, {kwargs}\n")
                else:
                    error_type = type(e).__name__
                    print(f"{func.__name__} error: {error_type}. Inputs {args}, {kwargs}\n")
                raise e
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> float:
    return x / y


print(my_function(2, 4))
