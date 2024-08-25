"""Дополнительное практическое задание по модулю: 'Наследование классов.'"""
import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, sides: list):
        self.__color = [color[0], color[1], color[2]]
        self.__sides = sides
        self.filled = True

    def set_sides(self, *new_sides):
        sides_list = []
        sides_list.extend(new_sides)
        if isinstance(sides_list[0], list):
            sides_list_add = sides_list[0]
        else:
            sides_list_add = sides_list
        if self.sides_count == 1:
            # length = 0.0
            if not self.__is_valid_sides(sides_list_add) == False and len(sides_list_add) == self.sides_count:
                self.__sides = sides_list_add
                sides_list_add_float = [float(x) for x in sides_list_add]
                length = sides_list_add_float[0]
            else:
                self.__sides = self.__sides
                length = self.__sides[0]
            _Circle__radius = length / (2 * 3.14)

        elif self.sides_count == 3:
            if not self.__is_valid_sides(sides_list_add) == False and len(sides_list_add) == self.sides_count:
                self.__sides = sides_list_add
            else:
                self.__sides = self.__sides

        elif self.sides_count == 12:
            if not self.__is_valid_sides(sides_list_add) == False and len(sides_list_add) == 1:
                self.__sides = [sides_list_add[0] for _ in range(12)]
            else:
                self.__sides = self.__sides

    def __is_valid_sides(self, sides: list):
        # sides_list = []
        # is_valid_sides_list = []
        if isinstance(self.__sides, int):
            sides_list = [self.__sides]
        else:
            sides_list = self.__sides
        if isinstance(sides, int):
            is_valid_sides_list = [sides]
        else:
            is_valid_sides_list = sides
        flag_is_valid_sides = True
        for is_valid_sides_element in is_valid_sides_list:
            if is_valid_sides_element == 0:
                flag_is_valid_sides = False
        if flag_is_valid_sides == True and len(sides_list) == len(is_valid_sides_list):
            self.__sides = is_valid_sides_list
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        global perimeter
        if self.sides_count == 1:
            perimeter = self.__sides[0]
        if self.sides_count == 3:
            perimeter = self.__sides[0] + self.__sides[1] + self.__sides[2]
        if self.sides_count == 12:
            perimeter = self.__sides[0] * 12
        return perimeter

    def __is_valid_color(self, *color):
        new_color_list: list = []
        new_color_list.extend(*color)
        if (0 <= new_color_list[0] <= 255) and (0 <= new_color_list[1] <= 255) and (0 <= new_color_list[2] <= 255):
            return True
        else:
            return False

    def set_color(self, *color):
        new_color_list: list = []
        new_color_list.extend(color)
        if not self.__is_valid_color(color) == False:
            self.__color = new_color_list
        else:
            self.__color = self.__color

    def get_color(self):
        return self.__color


class Circle(Figure):
    sides_count = 1
    __radius = None

    def __init__(self, color, *sides, __radius=None):
        sides_list = []
        sides_list.extend(sides)
        if len(sides_list) == self.sides_count:
            self.__sides = sides_list
        else:
            sides_list = [1]
            self.__sides = sides_list
        super().__init__(color, self.__sides)
        super().set_sides(self.__sides)
        super().get_sides()
        self.__radius = self.sides_count / (2.0 * math.pi)

    def get_square(self):
        length_list = self.get_sides()
        length = length_list[0]
        square = length ** 2 / (4 * math.pi)
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        sides_list = []
        sides_list.extend(sides)
        if len(sides_list) == self.sides_count:
            self.__sides = sides_list
        else:
            self.__sides = [1 for _ in range(3)]
        super().__init__(color, self.__sides)
        super().set_sides(self.__sides)
        super().get_sides()

    def get_square(self):
        length_list = self.get_sides()
        half_meter = (1 / 2) * (length_list[0] + length_list[1] + length_list[2])
        square = math.sqrt(half_meter * (half_meter - length_list[0]) *
                           (half_meter - length_list[1]) * (half_meter - length_list[2]))
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        sides_list = []
        sides_list.extend(sides)
        if len(sides_list) == 1:
            self.__sides = sides_list
        else:
            self.__sides = [1 for _ in range(12)]
        super().__init__(color, self.__sides)
        super().set_sides(self.__sides)
        super().get_sides()

    def get_volume(self):
        length_list = self.get_sides()
        volume = length_list[0] * length_list[0] * length_list[0]
        return volume


circle1 = Circle((200, 200, 100), 10)       # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)                     # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)                      # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)               # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)                                   # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# мои проверки
# print(f'{"Circle":=^30}')
# circle1 = Circle((200, 200, 100), 10, 14)
# print(circle1.get_sides())
# circle1.set_sides(15)
# print(circle1.get_sides())
# print(circle1.get_square())
# print(len(circle1))
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# print(f'{"Triangle":=^30}')
# triangle_1 = Triangle((200, 200, 100), 10, 6)
# print(triangle_1.get_color())
# print(triangle_1.get_sides())
# triangle_1.set_sides(10, 5, 8)
# print(triangle_1.get_sides())
# print(len(triangle_1))
# triangle_1.set_color(100, 150, 45)
# print(triangle_1.get_color())
# print(triangle_1.get_square())
# print(f'{"Cube":=^30}')
# cube1 = Cube((222, 35, 130), 6)
# print(cube1.get_color())
# print(cube1.get_sides())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
# cube1.set_color(150, 70, 15) # Изменится
# print(cube1.get_color())
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# print(len(cube1))
# print(cube1.get_volume())
