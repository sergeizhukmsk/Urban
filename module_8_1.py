# Модуль №8 Исключения Домашнее задание 1

def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return f'{a} + {b}'
        else:
            raise TypeError("Типы аргументов несовместимы")
    except TypeError as exc:
        print(exc)
        return None


# Примеры использования
print(add_everything_up(123.456, 'строка'))  # '123.456строка'
print(add_everything_up('яблоко', 4215))      # 'яблоко4215'
print(add_everything_up(123.456, 7))           # 130.456


### Объяснение:
# Функция сначала проверяет, являются ли оба аргумента числами (тип `int` или `float`).
# Если это так, она возвращает их сумму.
# Если оба аргумента являются строками, функция объединяет их и возвращает результат.
# Если типы аргументов разные (число и строка), функция возвращает строковое представление обоих аргументов,
# объединенных в порядке их передачи.


