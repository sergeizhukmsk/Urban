class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def feed(self, plant):
        if not self.fed:
            if plant.edible:
                print(f"{self.name} съел {plant.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {plant.name}")
                self.alive = False


class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)


# Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)

