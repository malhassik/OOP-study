from math import pi


class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        print(f"{self.name}: площадь = {round(self.area(), 2)}")


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    # Геттер для width
    @property
    def width(self):
        return self._width

    # Сеттер для width
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self._height = value

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радиус должен быть положительным")
        self._radius = value

    def area(self):
        return pi * self.radius**2
