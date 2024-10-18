# Модуль №9 Домашнее задание 1

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        try:
            result = func(int_list)
            results[func.__name__] = result
        except (TypeError, ValueError):
            results[func.__name__] = 'Функция не может быть применена к списку'

    return results


# Пример работы функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

