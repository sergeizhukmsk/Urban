class Vehicle:
    __COLOR_VARIANTS = ['white', 'black', 'red', 'green', 'blue']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color if color.lower() in map(str.lower, self.__COLOR_VARIANTS) else 'black'

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self) -> None:
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str) -> None:
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)

# Пример использования классов
sedan = Sedan(owner='Иван', model='Toyota Camry', engine_power=200, color='blue')
sedan.print_info()

# Изменение цвета на допустимый
sedan.set_color('green')
sedan.print_info()

# Попытка изменить цвет на недопустимый
sedan.set_color('purple')
sedan.print_info()


# ###Класс `Vehicle`:**
#    - Содержит атрибуты `owner`, `__model`, `__engine_power`, `__color` и класс-атрибут `__COLOR_VARIANTS`.
#    - Методы `get_model`, `get_horsepower`, `get_color` возвращают соответствующую информацию о транспортном средстве.
#    - Метод `print_info` выводит информацию о транспортном средстве и его владельце.
#    - Метод `set_color` позволяет изменить цвет, если новый цвет есть в списке допустимых цветов.
#
# ###Класс `Sedan`:**
#    - Наследует класс `Vehicle`.
#    - Содержит атрибут `__PASSENGERS_LIMIT`, который указывает на максимальное количество пассажиров в седане.
#    - Конструктор `__init__` вызывает конструктор родительского класса с помощью `super()`.
#
# ### Пример использования:
# - Создается объект класса `Sedan` с заданными параметрами.
# - Вызываются методы для отображения информации и изменения цвета. Если цвет не допустимый, выводится соответствующее сообщение.
