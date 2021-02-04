'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'{self.name}: цвет {self.color}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed} км/ч.'


class TownCar(Car):
    # Городской автомобиль

    def show_speed(self):
        return f'{self.name} превысил скорость! Ваша скорость: {self.speed} км/ч! ' \
               f'Необходимо снизить до 60км/ч' if self.speed > 60 else \
               f"{self.name}: Скорость автомобиля {self.speed} км/ч"


class WorkCar(Car):
    #Грузовой автомобиль

    def show_speed(self):
        return f'{self.name} превысил скорость! Ваша скорость: {self.speed} км/ч! ' \
               f'Необходимо снизить до 40км/ч' if self.speed > 40 else \
               f"{self.name}: Скорость автомобиля {self.speed}"


class SportCar(Car):
    # Спортивный автомобиль

    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)
        print(f'{self.color} {self.name}  несется со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    # Полицейский автомобиль

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)
        print('Включаем мигалку и сирену! Ловим нарущителей!')


police_car = PoliceCar('Полицейский автомобиль', 'сине-белый', 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(1)
police_car.stop()
print()

work_car = WorkCar('Камаз', 'оранжевый', 50)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = SportCar('Hennessey Venom GT', 'черный', 350)
sport_car.go()

sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('Лада', 'зеленый', 80)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()
print()

town_car_1 = TownCar('Нива', 'серый', 60)
print(town_car_1.show_speed())



