class House:
    number_of_floors: object

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor+1):
                print(floor)


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название: {self.name} кол-во этажей: {self.number_of_floors}'


# Должен возвращать True, если количество этажей одинаковое у self и у other
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors


    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors


    def __add__(self, value):
        if not isinstance(value, int):
            print("Значение должно быть целым числом")

        self.number_of_floors += value
        return self


    def __iadd__(self, value):
        if not isinstance(value, int):
            print("Значение должно быть целым числом")

        self.number_of_floors += value
        return self

    def __radd__(self, value):
        if not isinstance(value, int):
            print("Значение должно быть целым числом")

        self.number_of_floors += value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

# __add__
h1 = h1 + 10
print(h1)
print(h1 == h2)

# __iadd__
h1 += 10
print(h1)

# __radd__
h2 = 10 + h2
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

"""
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False
"""
