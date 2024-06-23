"""
Домашнее задание по теме "Множественное наследование"
"""


class Vehicle:
    """
    класс Vehicle транспортных средств, родительский, базовый
    """
    vehicle_type = None


class Car:
    """
    класс Car машин, родительский, базовый
    """
    price = 1000000

    def __init__(self, price, power):
        self.power = power

    def horce_powers(self):

        h_power: float = self.power * 1.3596
        return h_power


class Nissan(Car, Vehicle):
    """
    класс Nissan модель автомобиля, наследник класса Car и Vehicle
    """
    def __init__(self, price, vehicle_type, power):
        super().__init__(price, power)
        super().horce_powers()
        Vehicle.__init__(self.vehicle_type)
        self.price = price
        self.vehicle_type = vehicle_type
        self.power = power


if __name__ == '__main__':

    nissan = Nissan('автомобиль', 2500000, 150)
    print(nissan.vehicle_type)
    print(nissan.price)
    print(nissan.power)
    print(nissan.horce_powers())

    print(Vehicle.vehicle_type)
    print(Car.price)
