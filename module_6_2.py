class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color if color.lower() in map(str.lower, self.__COLOR_VARIANTS) else 'black'


    def get_model(self):
        return f"Модель: {self.__model}"


    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"


    def get_color(self):
        return f"Цвет: {self.__color}"


    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")


    def set_color(self, new_color):
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)

# Пример использования классов
# sedan = Sedan(owner='Иван', model='Toyota Camry', engine_power=200, color='blue')
# sedan.print_info()
#
# # Изменение цвета на допустимый
# sedan.set_color('green')
# sedan.print_info()
#
# # Попытка изменить цвет на недопустимый
# sedan.set_color('purple')
# sedan.print_info()

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

