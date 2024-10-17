# Модуль №8 Исключения Домашнее задание 2

def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number  # Пытаемся добавить число к результату
        except TypeError:
            incorrect_data += 1  # Увеличиваем счётчик некорректных данных при ошибке
            print('Некорректный тип данных для подсчёта суммы -', number)

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if not hasattr(numbers, '__iter__'):
            print('В numbers записан некорректный тип данных')
            return None

        total_sum, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data  # Учитываем только корректные данные

        # Вычисляем среднее арифметическое
        return total_sum / count if count > 0 else 0

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Примеры вызова функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


