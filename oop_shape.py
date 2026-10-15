from math import pi


class Shape:

    # Контруктор класса
    def __init__(self, name):
        self.name = name

    # Методы
    def area(self):
        return 0

    def info(self):
        print(f"{self.name}: площадь = {round(self.area(), 2)}")

    def __str__(self):
        return f"Фигура: {self.name}"


class Rectangle(Shape):

    # Контруктор класса
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

    # Геттер для height
    @property
    def height(self):
        return self._height

    # Сеттер для height
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self._height = value

    # Геттер для функции периметр
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    # Методы
    def __str__(self):
        return f"Прямоугольник {self.width}×{self.height}"

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.height == other.height

    def area(self):
        return self.width * self.height


class Circle(Shape):

    # Контруктор класса
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    # Геттер для radius
    @property
    def radius(self):
        return self._radius

    # Сеттер для radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радиус должен быть положительным")
        self._radius = value

    # Методы
    def __str__(self):
        return f"Круг с радиусом {self.radius}"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def area(self):
        return pi * self.radius**2
