class Human:
    def __init__(self, name, age = 0):
        self.name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say('Hello, I am {}'.format(self.name))

    def how_old(self):
        self._say('I am {} years old'.format(self._age))


#example

bob = Human('Bob', age = 31)
bob.say_name()
bob.how_old()
