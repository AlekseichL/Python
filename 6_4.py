class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print('Машина повернула направо')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed} км/ч')

#TownCar, SportCar, WorkCar, PoliceCar
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed} км/ч')
        if self.speed>60:
            print('Превышение скорости движения автомобиля')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed} км/ч')
        if self.speed>40:
            print('Превышение скорости движения автомобиля')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

a = TownCar(55, 'Черный', 'Mazda', False)
print(f'Марка автомобиля: {a.name}, цвет: {a.color}')
a.go()
a.show_speed()
a.turn()
a.stop()

print('')
a2 = TownCar(63, 'Красный', 'BMW', False)
print(f'Марка автомобиля: {a2.name}, цвет: {a2.color}')
a2.go()
a2.show_speed()
a2.turn()
a2.stop()

print('')
s=SportCar(120, 'Синий', 'Mercedes', False)
print(f'Марка автомобиля: {s.name}, цвет: {s.color}')
s.go()
s.show_speed()
s.turn()
s.stop()

print('')
w=WorkCar(43, 'Черный', 'GMC', False)
print(f'Марка автомобиля: {w.name}, цвет: {w.color}')
w.go()
w.show_speed()
w.turn()
w.stop()

print('')
p=PoliceCar(73, 'Черный', 'Ford', True)
print(f'Марка автомобиля: {p.name}, цвет: {p.color}')
p.go()
p.show_speed()
p.turn()
p.stop()
