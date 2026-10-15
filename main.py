from oop_shape import Shape, Rectangle, Circle

# Работа с классом Rectangle
rectangle = Rectangle(5, 5)
print(rectangle)  # Прямоугольник 5×10
print(repr(rectangle))  # Rectangle(width=5, height=10)

circle = Circle(5)
print(circle)  # Круг с радиусом 5

r1 = Rectangle(5, 10)
r2 = Rectangle(5, 10)
r3 = Rectangle(3, 3)

print(r1 == r2)
print(r1 == r3)
