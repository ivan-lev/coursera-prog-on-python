class Human:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
    def __repr__(self):
        return self.name

class Planet:
    def __init__(self, name, population = None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print('Welcome to {}, {}'.format(self.name, human.name))
        self.population.append(human)
        
    def who_live(self):
        print('Here are {} people on {}:'.format(len(self.population), self.name))
        print(self.population)
              

# example
mars = Planet('Mars')
bob = Human('Bob')
mars.add_human(bob)

mars.who_live()
