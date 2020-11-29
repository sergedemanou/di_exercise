# Old MacDonald’s Farm

class Farm():
    def __init__(self, name):
        self.name = name
        self.animals = {}


    def add_animal(self, name, number = 1):
        if name in self.animals:
            k = self.animals[name]
            self.animals.update({name: k + number})
        else:
            self.animals[name] = number

        """for i in self.animals:
            print('{} : {}'.format(i, self.animals[i]))"""

    def get_info(self):
        print('E-I-E-I-0!')

    def get_animal_types(self):
        tab = []
        for i in self.animals:
            tab.append(i)
        return sorted(tab)

    def get_short_info(self):
        tab = self.get_animal_types()
        tab1 = ', '.join(tab[:-1])+ ' and' + ' ' + tab[-1] + '.'
        print('{}\'s farm has {}'.format(self.name, tab1))


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.animals)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())

