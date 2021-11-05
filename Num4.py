class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go():
        print('поехала')

    def stop():
        print('остановилась')

    def turn(self, direction):
        print('повернула', direction)

    def show_speed(self):
        print('Текущая скорость', self.speed, 'км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышена допустимая скорость в 60 км/ч ({self.speed})')
        else:
            print(f'Текущая скорость {self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышена допустимая скорость в 40 км/ч ({self.speed})')
        else:
            print(f'Текущая скорость {self.speed} км/ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


sport = SportCar(100, 'yellow', 'Camaro', False)
town = TownCar(70, 'blue', 'Focus', False)
work = WorkCar(30, 'yellow', 'Combilift', False)
police = PoliceCar(120, 'yellow', 'Lamborghini', True)


sport.show_speed()
town.show_speed()
work.show_speed()
police.show_speed()
police.turn('направо')
print(police.color)
