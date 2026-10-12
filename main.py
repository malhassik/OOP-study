from oop_shape import Shape, Rectangle, Circle

# Работа с классом Shape
rectangle = Rectangle(5, 5)
circle = Circle(5)

try:
    rectangle.width = -5
    print("Ошибка не сработала!")
except ValueError as e:
    print("Ошибка:", e)

try:
    rectangle.height = 0
    print("Ошибка не сработала!")
except ValueError as e:
    print("Ошибка:", e)

try:
    circle.radius = -1
    print("Ошибка не сработала!")
except ValueError as e:
    print("Ошибка:", e)
