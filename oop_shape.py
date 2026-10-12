from math import pi


class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        print(f"{self.name}: площадь = {self.area()}")


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def area(self):
        return pi * self.radius**2
