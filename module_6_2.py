"""
Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
Цели: Применить сокрытие атрибутов и повторить наследование. Рассмотреть на примере объекта из реального мира.

Задача "Изменять нельзя получать":
В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет, мощность двигателя и
прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных сервисах. Да, узнать
значения этих свойств мы сможем, но вот изменить - нет.

Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса
Vehicle.

Пункты задачи:
1. Создайте классы Vehicle и Sedan.
2. Напишите соответствующие свойства в обоих классах.
3. Не забудьте сделать Sedan наследником класса Vehicle.
4. Создайте объект класса Sedan и проверьте, как работают все его методы, взятые из класса Vehicle.
"""

from colorama import init, Fore, Back, Style


class Vehicle:
    """
    класс транспорта
    1. Атрибут owner(str) - владелец транспорта. (владелец может меняться)
    2. Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
    3. Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    4. Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
    А так же атрибут класса:
    1. Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания.
    1. Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
    2. Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    3. Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    4. Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
    а так же владельца в конце в формате "Владелец: <имя>"
    5. Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в
    списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
    Взаимосвязь методов и скрытых атрибутов:
    1. Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
    __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
    2. Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
    3. Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
    """
    __COLOR_VARIANTS = ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN"]

    def __init__(self, owner, model, engine_power, color):
        self.owner: str = owner
        self.__model: str = model
        self.__engine_power: int = engine_power
        self.__color: str = color
        self.__COLOR_VARIANTS = Vehicle.__COLOR_VARIANTS


    def get_model(self):
        """
        Метод get_model - возвращает строку с названием модели транспорта
        :return: "Модель: <название модели транспорта>"
        """
        for i in range(len(self._Vehicle__COLOR_VARIANTS)):
            if self.__color.upper() == self._Vehicle__COLOR_VARIANTS[i]:
                if self.__color.upper() == 'BLACK':
                    return print(Fore.BLACK + f'Модель: {self.__model}')
                elif self.__color.upper() == 'RED':
                    return print(Fore.RED + f'Модель: {self.__model}')
                elif self.__color.upper() == 'GREEN':
                    return print(Fore.GREEN + f'Модель: {self.__model}')
                elif self.__color.upper() == 'YELLOW':
                    return print(Fore.YELLOW + f'Модель: {self.__model}')
                elif self.__color.upper() == 'BLUE':
                    return print(Fore.BLUE + f'Модель: {self.__model}')
                elif self.__color.upper() == 'MAGENTA':
                    return print(Fore.MAGENTA + f'Модель: {self.__model}')
                elif self.__color.upper() == 'CYAN':
                    return print(Fore.CYAN + f'Модель: {self.__model}')
                else:
                    return print(Fore.RESET + f'Модель: {self.__model}')

    def get_horsepower(self):
        """
        Метод get_horsepower - возвращает строку с указанием мощности двигателя транспорта
        :return: "Мощность двигателя: <мощность>"
        """
        for i in range(len(self._Vehicle__COLOR_VARIANTS)):
            if self.__color.upper() == self._Vehicle__COLOR_VARIANTS[i]:
                if self.__color.upper() == 'BLACK':
                    return print(Fore.BLACK + f'Мощность двигателя: {self.__engine_power}')
                elif self.__color.upper() == 'RED':
                    return print(Fore.RED + f'Мощность двигателя: {self.__engine_power}')
                elif self.__color.upper() == 'GREEN':
                    return print(Fore.GREEN + f'Мощность двигателя: {self.__engine_power}')
                elif self.__color.upper() == 'YELLOW':
                    return print(Fore.YELLOW + f'Мощность двигателя: {self.__engine_power}')
                elif self.__color.upper() == 'BLUE':
                    return print(Fore.BLUE + f'Мощность двигателя: {self.__engine_power}')
                elif self.__color.upper() == 'MAGENTA':
                    return print(Fore.MAGENTA + f'Мощность двигателя: {self.__engine_power}')
                elif self.__color.upper() == 'CYAN':
                    return print(Fore.CYAN + f'Мощность двигателя: {self.__engine_power}')
                else:
                    return print(Fore.RESET + f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        """
        Метод get_color - возвращает строку с указанием цвета транспорта
        :return: "Цвет: <цвет транспорта>"
        """
        for i in range(len(self._Vehicle__COLOR_VARIANTS)):
            if self.__color.upper() == self._Vehicle__COLOR_VARIANTS[i]:
                if self.__color.upper() == 'BLACK':
                    return print(Fore.BLACK + f'Цвет: {self.__color.upper()}')
                elif self.__color.upper() == 'RED':
                    return print(Fore.RED + f'Цвет: {self.__color.upper()}')
                elif self.__color.upper() == 'GREEN':
                    return print(Fore.GREEN + f'Цвет: {self.__color.upper()}')
                elif self.__color.upper() == 'YELLOW':
                    return print(Fore.YELLOW + f'Цвет: {self.__color.upper()}')
                elif self.__color.upper() == 'BLUE':
                    return print(Fore.BLUE + f'Цвет: {self.__color.upper()}')
                elif self.__color.upper() == 'MAGENTA':
                    return print(Fore.MAGENTA + f'Цвет: {self.__color.upper()}')
                elif self.__color.upper() == 'CYAN':
                    return print(Fore.CYAN + f'Цвет: {self.__color.upper()}')
                else:
                    return print(Fore.RESET + f'Цвет: {self.__color.upper()}')

    def print_info(self):
        """
        Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
        а так же владельца в конце в формате "Владелец: <имя>"
        :return:
        """
        self.get_model()
        self.get_horsepower()
        self.get_color()
        for i in range(len(self._Vehicle__COLOR_VARIANTS)):
            if self.__color.upper() == self._Vehicle__COLOR_VARIANTS[i]:
                if self.__color.upper() == 'BLACK':
                    return print(Fore.BLACK + f'Владелец: {self.owner}')
                elif self.__color.upper() == 'RED':
                    return print(Fore.RED + f'Владелец: {self.owner}')
                elif self.__color.upper() == 'GREEN':
                    return print(Fore.GREEN + f'Владелец: {self.owner}')
                elif self.__color.upper() == 'YELLOW':
                    return print(Fore.YELLOW + f'Владелец: {self.owner}')
                elif self.__color.upper() == 'BLUE':
                    return print(Fore.BLUE + f'Владелец: {self.owner}')
                elif self.__color.upper() == 'MAGENTA':
                    return print(Fore.MAGENTA + f'Владелец: {self.owner}')
                elif self.__color.upper() == 'CYAN':
                    return print(Fore.CYAN + f'Владелец: {self.owner}')
                else:
                    return print(Fore.RESET + f'Владелец: {self.owner}')

    def set_color(self, new_color):
        """
        Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в
        списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
        :param new_color:
        :return:
        """
        new_color = new_color.upper()
        self.__color = new_color
        for i in range(len(self._Vehicle__COLOR_VARIANTS)):
            if new_color == self._Vehicle__COLOR_VARIANTS[i]:
                if self.__color == 'BLACK':
                    return self.__color
                elif self.__color == 'RED':
                    return self.__color
                elif self.__color == 'GREEN':
                    return self.__color
                elif self.__color == 'YELLOW':
                    return self.__color
                elif self.__color == 'BLUE':
                    return self.__color
                elif self.__color == 'MAGENTA':
                    return self.__color
                elif self.__color == 'CYAN':
                    return self.__color
            else:
                if i == len(self._Vehicle__COLOR_VARIANTS) - 1:
                    return print(Fore.RESET + f'Невозможно покрасить в {self.__color.upper()}')


class Sedan(Vehicle):
    """
    Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
    Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)
    """
    __PASSENGERS_LIMIT = 5


if __name__ == '__main__':
    init(autoreset=True) # Для поддержки вывода на Windows 10

    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'magenta')
    #   изначальные свойства
    vehicle1.print_info()
    #   меняем свойства
    vehicle1.set_color('Pink')

    vehicle1.set_color('red')
    vehicle1.owner = 'Vasyok'
    vehicle1.print_info()
    print(vehicle1._Sedan__PASSENGERS_LIMIT)


