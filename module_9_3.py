# Модуль №9 Домашнее задание 3

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(s1) - len(s2) for s1, s2 in zip(first, second) if len(s1) != len(s2))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)) if i < len(second))




# Вывод результатов
print(list(first_result))  # Вывод разниц длин строк
print(list(second_result))  # Вывод разниц длин строк из одинаковых позиций


