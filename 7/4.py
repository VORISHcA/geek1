class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} тронулась'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} право руля'

    def turn_left(self):
        return f'{self.name} лево руля'

    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')

        if self.speed > 40:
            return f'{self.name} высокая'
        else:
            return f'{self.name} нормальная'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')

        if self.speed > 60:
            return f'{self.name} высокая'
        else:
            return f'{self.name} нормальная'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская'
        else:
            return f'{self.name} не полицейская'


test1 = TownCar(100, 'цвет1', 'тип1', False)
test2 = WorkCar(100, 'цвет2', 'тип2', False)
test3 = PoliceCar(100, 'цвет3',  'тип3', True)
print(test1.turn_left())
print(test1.go())
print(test3.show_speed())
print(test3.police())
print(test2.color)
