class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 0:
            print(f'Машина марки {self.name} едет со скростью {self.speed} км/ч')
        elif self.speed == 0:
            print(f'Машина марки {self.name} стоит')
        else:
            print(f'Машина марки {self.name} сдаёт назад со скростью {abs(self.speed)} км/ч')

    def show_info(self):
        print(f'Марка: {self.name}\tскрость: {abs(self.speed)}\t км/ч цвет: {self.color}\t полицейская: {self.is_police}')

    def go(self, speed):
        self.speed = speed
        print(f'Машина марки {self.name} поехала со скростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Машина марки {self.name} остановилась')

    def turn(self, direct):
        print(f'Машина марки {self.name} повернула {direct}')


class TownCar(Car):
    def show_speed(self):
        s_limit = 60
        if self.speed > s_limit:
            print(f'[ПРЕВЫШЕНИЕ 60] Машина марки {self.name} превысила ограничение на {self.speed - s_limit} км/ч')
        elif self.speed > 0:
            print(f'Машина марки {self.name} едет со скростью {self.speed} км/ч')
        elif self.speed == 0:
            print(f'Машина марки {self.name} стоит')
        else:
            print(f'Машина марки {self.name} сдаёт назад со скростью {abs(self.speed)} км/ч')


class WorkCar(Car):
    def show_speed(self):
        s_limit = 40
        if self.speed > s_limit:
            print(f'[ПРЕВЫШЕНИЕ 60] Машина марки {self.name} превысила ограничение на {self.speed - s_limit} км/ч')
        elif self.speed > 0:
            print(f'Машина марки {self.name} едет со скростью {self.speed} км/ч')
        elif self.speed == 0:
            print(f'Машина марки {self.name} стоит')
        else:
            print(f'Машина марки {self.name} сдаёт назад со скростью {abs(self.speed)} км/ч')


class SportCar(Car):
    def show_speed(self):
        s_limit = 1224
        if self.speed > s_limit:
            print(f'[Превышено число Маха] превышение на {self.speed - s_limit} км/ч')
        elif self.speed > 0:
            print(f'Машина марки {self.name} едет со скростью {self.speed} км/ч')
        elif self.speed == 0:
            print(f'Машина марки {self.name} стоит')
        else:
            print(f'Машина марки {self.name} сдаёт назад со скростью {abs(self.speed)} км/ч')


class PoliceCar(Car):
    def show_info(self):
        print(f'Полицейская машина марки: {self.name}\tскрость: {abs(self.speed)}\t км/ч цвет: {self.color}\t')


ferrari = SportCar(100, 'красный', 'Ferrari F430', False)
ferrari.show_speed()
ferrari.turn('налево')
ferrari.stop()
ferrari.show_speed()
print('\n')
probox = TownCar(110, 'черный', 'Toyota Probox', False)
probox.show_speed()
probox.go(55)
probox.stop()
probox.show_speed()
print('\n')
komatsu = WorkCar(31, 'желтый', 'Komatsu wb93r', False)
komatsu.show_speed()
komatsu.turn('направо')
komatsu.speed = 0  # доступ к атрибуту
komatsu.show_speed()
komatsu.show_info()
print('\n')
corolla = PoliceCar(-5, 'белый', 'Toyota Corolla', True)
corolla.show_speed()
corolla.show_info()
