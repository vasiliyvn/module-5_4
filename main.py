class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self,name,numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def __del__(self):
        # return f'{self.name} снесён, но он останется в истории'
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3
print(House.houses_history)
del h1