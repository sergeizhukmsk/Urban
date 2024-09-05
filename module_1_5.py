# Задайте переменные разных типов данных:
# Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
# Выполните операции вывода кортежа immutable_var на экран.
# Изменение значений переменных:
# Попытайтесь изменить элементы кортежа immutable_var.
# Объясните, почему нельзя изменить значения элементов кортежа.
# Создание изменяемых структур данных:
# Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# Измените элементы списка mutable_list.
# Выведите на экран измененный список mutable_list.

immutable_var = ('september', 'kaluga', 5, 10, 25, True, False)
print(immutable_var)
# immutable_var[1] = 'kursk'
# TypeError: 'tuple' object does not support item assignment
print(immutable_var)
# Кортежи в Python являются неизменяемыми структурами данных, что означает,
# что их элементы нельзя изменить после создания кортежа.

immutable_list = ['september', 'kaluga', 5, 10, 25, True, False]
print(immutable_list)
immutable_list[1] = 'kursk'
print(immutable_list)

