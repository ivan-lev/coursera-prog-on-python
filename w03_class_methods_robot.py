class Robot:
    def __init__(self, power):
        self._power = power

        power = property()

        @power.setter
        def power(self, value):
            if value < 0:
                self._power = 0
            else:
                self._power = value

        @power.getter
        def power(self):
            return self._power

        @power.deleter
        def power(self):
            print('Powerless robot is useless robot')
            del self._power


#example
robot = Robot(120)
robot.power = -20
print(robot.power)
