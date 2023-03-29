class ColoredMixin:
    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color


class MotorizedMixin:
    def __init__(self, motor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.motor = motor


class Car:

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model



class SportsCar(MotorizedMixin, ColoredMixin, Car):
    def __init__(self, leap_time, manufacturer, model, color, motor):
        self.leap_time = leap_time
        super().__init__(motor, color, manufacturer, model)


s = SportsCar(5, 'porshe', '911', 'red', 'v8')
print(SportsCar.__mro__)
print(s)