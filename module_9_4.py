# Модуль №9 Домашнее задание 4

### 1. Lambda-функция для совпадения букв в строках
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y:x == y, first, second))
print(result)


### 2. Замыкание для записи в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(f"{data}\n")

    return write_everything

# Пример использования
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


### 3. Класс MysticBall с методом call

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

