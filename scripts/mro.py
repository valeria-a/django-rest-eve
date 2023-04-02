class Colored:
    def __init__(self, color='transparent'):
        self.color = color


class Motorized:
    def __init__(self, motor):
        self.motor = motor


class Car:

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model



class SportsCar(Car, Motorized, Colored):
    def __init__(self, leap_time, manufacturer, model, color, motor):
        # super().__init__(manufacturer, model)
        # super(Car, self).__init__(motor)
        # super(Motorized, self).__init__(color)


        Car.__init__(self, manufacturer, model)
        Motorized.__init__(self, motor)
        Colored.__init__(self, color)
        self.leap_time = leap_time



s = SportsCar(5, 'porshe', '911', 'red', 'v8')
print(s)
print(s.motor)
print(s.leap_time)
print(s.color)
