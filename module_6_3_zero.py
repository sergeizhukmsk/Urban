class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


# Создание объекта класса Pegasus
class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


pegasus = Pegasus()

# Проверка работы методов
print("Начальная позиция:", pegasus.get_pos())

# Вызываем методы
pegasus.run(10)
print("После бега:", pegasus.get_pos())

pegasus.fly(5)
print("После полета:", pegasus.get_pos())

pegasus.move(15, 10)
print("После движения:", pegasus.get_pos())

# Проверка звука
print("Звук пегаса:", end=' ')
pegasus.voice()


# ### Пояснение к коду:
# 1. **Класс `Horse`**:
#    - Имеет атрибуты `x_distance` и `sound`.
#    - Метод `run(dx)` увеличивает `x_distance` на `dx`.
#
# 2. **Класс `Eagle`**:
#    - Имеет атрибуты `y_distance` и `sound`.
#    - Метод `fly(dy)` увеличивает `y_distance` на `dy`.
#
# 3. **Класс `Pegasus`**:
#    - Наследует `Horse` и `Eagle`.
#    - В конструкторе инициализирует оба родительских класса.
#    - Метод `move(dx, dy)` вызывает методы `run` и `fly`.
#    - Метод `get_pos()` возвращает текущее положение в виде кортежа.
#    - Метод `voice()` выводит звук, унаследованный от родительских классов.

### Результат выполнения:
#При запуске этого кода вы увидите, как изменяется позиция пегаса после каждого вызова методов, а также его звук.

