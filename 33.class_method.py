class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)


p1 = Person("Emil")
p1.greet()


class Calculator:
    def add(self, a, b):
        return a+b

    def multiply(self, a, b):
        return a*b


calc = Calculator()

print(calc.multiply(3, 5))
print(calc.add(3, 5))


class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"


p1 = Person1("Tobias", 28)
print(p1.get_info())


class Person2:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")


p1 = Person2("Emil")

del Person2.greet

p1.greet()  # This will cause an error
