"""
Домашнее задание по теме "Множественное наследование"
"""


class Vehicle:
    """
    класс Vehicle транспортных средств, родительский, базовый
    """
    def __init__(self, vehicle_type=None):
        self.vehicle_type: str = vehicle_type


class Car:
    """
    класс Car машин, родительский, базовый
    """
    price: int = 1000000

    def __init__(self, price, horsepower_for_car):
        self.price = price
        self.horsepower_for_car: int = horsepower_for_car

    def horce_powers(self):
        print(f'У автомобиля {self.horsepower_for_car} лошадинных сил')


class Nissan(Vehicle, Car):
    """
    класс Nissan модель автомобиля, наследник класса Car и Vehicle
    """
    def __init__(self, vehicle_type, price, horsepower_for_car):
        super().__init__(vehicle_type)
        Car.__init__(self, price, horsepower_for_car)
        Car.horce_powers(self)


if __name__ == '__main__':

    vehicle = Vehicle()
    car = Car(0, 0)
    nissan = Nissan('автомобиль', 2500000, 267)
    print(nissan.vehicle_type)
    print(nissan.price)
