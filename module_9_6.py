# Модуль №9 Домашнее задание 6

def all_variants(text):
    if not isinstance(text, str):
        raise TypeError('Аргумент должен быть строкой')

    n = len(text)

    for length in range(1, n + 1):
        for start in range(n - length + 1):
            end = start + length
            subsequence = text[start:end]
            yield subsequence


# Пример использования функции
a = all_variants("abc")
for i in a:
    print(i)


