# Класс животных
class Animal:
    alive = True  # живой
    fed = False  # накормленный

    def __init__(self, name):
        self.name = name # индивидуальное название каждого животного


    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# Класс растений
class Plant:
    edible = False  # съедобность
    def __init__(self, name):
        self.name = name # индивидуальное название каждого растения


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)



class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)



class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True # переопределить при наследовании


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

