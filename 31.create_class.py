# create a class

class MyClass:
    x = 5

# create an object


p1 = MyClass()
print(p1.x)

# del p1


# class Person:
#     pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
print(p1.name)
print(p1.age)


# Without the __init__() method, you would need to set properties manually for each object:

class Person1:
    pass


p1 = Person1()
p1.name = "shamim"
p1.age = 25

print(p1.name)
print(p1.age)


class Person2:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country


p1 = Person2("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)


# The self Parameter
# The self parameter is a reference to the current instance of the class.

# It is used to access properties and methods that belong to the class.

class PersonClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")


p1 = PersonClass("Satish", 25)
p1.greet()


# Why Use self?
# Without self, Python would not know which object's properties you want to access:


# self Does Not Have to Be Named "self"
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:

class PersonSelf:
    def __init__(abc, name, age):
        abc.name = name
        abc.age = age

    def greet(abc):
        print(f"Hello, my name is {abc.name}")


p1 = PersonSelf("Satish", 25)
p1.greet()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")


car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()
