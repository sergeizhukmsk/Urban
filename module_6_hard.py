import math

class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled):
        if len(str(sides)) != self.sides_count:
            sides = [1] * self.sides_count

        self.__color = color # список цветов в формате RGB
        self.__sides = sides # список сторон (целые числа)
        self.filled = filled # закрашенный, bool

    def get_color(self):
        return self.__color


    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректные значения цвета.")


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


    def __is_valid_sides(self, *new_sides):
        return all(side > 0 for side in new_sides) and len(new_sides) == self.sides_count


    def get_sides(self):
        return self.__sides


    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides, filled):
        super().__init__(color, sides, filled)
        self.__radius = sides # sides[0]


    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides, filled):
        super().__init__(color, sides, filled)
        self.__sides = sides #* self.sides_count

    def get_volume(self):
        return self.__sides ** 3

# Код для основной проверки circle1
circle1 = Circle((200, 200, 100), 10, True) # (Цвет, стороны)

# Проверка на изменение цветов circle1
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

# Код для основной проверки cube1
cube1 = Cube((222, 35, 130), 6, True)

# Проверка на изменение цветов cube1
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится !!!!!!
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра круга, это и есть длина circle1
print(len(circle1))

# Проверка объёма куба cube1
print(cube1.get_volume())


# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216

