# Задача 4 (сложно) "Первый после точки": Напишите в начале программы однострочный комментарий: "4th program".
# Дана строка '123.456'. Вывести на экран первую цифру после запятой - 4. Начало алгоритма решения:
# Преобразуйте в строку в дробное число. ('123.456' -> 123.456) Умножьте на 10, чтобы сместить 4 в целую часть. (1234.56)
# Следующие шаги алгоритма составьте самостоятельно.
# В них вам понадобится команда int() и остаточное деление на 10.

# 4th program
input_string = '123.456'
number_1 = float(input_string)
number_2 = number_1 * 10
integer_part = int(number_2)
result = integer_part % 10
print(result)
