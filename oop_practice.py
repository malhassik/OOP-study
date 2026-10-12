class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} говорит гав!")

    def birthday(self):
        self.age += 1

    def info(self):
        print(f"Собака {self.name}, возраст {self.age}")
