# Модуль №9 Домашнее задание 6

def all_variants(text):
    n = len(text)
    for i in range(2**n):
        subsequence = ''
        for j in range(n):
            if i // (2 ** j) % 2 == 1:
                subsequence += text[j]

        yield subsequence


# Пример использования функции
stroka = all_variants("abc")
for i in stroka:
    print(i)


