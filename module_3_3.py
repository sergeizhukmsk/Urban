def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # Без аргументов
print_params(b = 25)  # Только b
print_params(c = [1, 2, 3])  # Только c

values_list = ['строка', True, 42]  # Список разных типов
values_dict = {'a': 10, 'b': 'текст', 'c': False}  # Словарь с разными типами значений

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
