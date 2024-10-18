# Модуль №9 Домашнее задание 2

# Исходные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]
third_result = {string: len(string) for string in first_strings + second_strings if len(string) % 2 == 0}


# Вывод результатов
print(first_result)  # [8, 8, 8] (длину слов "Programmer", "Monitors", "Variable")
print(second_result)  # [] (пары строк одинаковой длины)
print(third_result)  # {'Programmer': 8, 'Monitors': 8, 'Computer': 8, 'Assembler': 9}


