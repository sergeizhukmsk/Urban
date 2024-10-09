# класс описывающий лошадь
class Horse:
    def __init__(self):
        self.x_distance = 0 # пройденный путь.
        self.sound = 'Frrr' # звук, который издаёт лошадь.


    def run(self, dx): # dx - изменение дистанции, увеличивает x_distance на dx
        self.x_distance += dx


# класс описывающий орла
class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


# Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке
class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

# где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)


    def voice(self):
        print(self.sound)


# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

