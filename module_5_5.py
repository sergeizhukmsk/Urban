class House_New:
    number_of_floors: object
    houses_history = []

    def __new__(cls, *args):
        instance = super().__new__(cls)
        instance.__init__(*args)
        cls.houses_history.append(args[0])  # Добавляем название здания в history
        cls.name = args[0]
        cls.number_of_floors = args[1]
        return instance


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


