# Class Properties
# Properties are variables that belong to a class. They store data for each object created from the class.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Satish", 25)

print(p1.name)
p1.age = 30

print(p1.age)
del p1.age
# print(p1.age) # This would cause an error


# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).

# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:


class Person2:
    species = "Human"  # Class property

    def __init__(self, name):
        self.name = name  # Instance property


p1 = Person2("Emil")
p2 = Person2("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)


class Person3:
    lastname = ""

    def __init__(self, name):
        self.name = name


p1 = Person3("Linus")
p2 = Person3("Emil")

Person3.lastname = "Refsnes"
print(p1.name)
print(p1.lastname)
print(p2.name)
print(p2.lastname)


# Add a new property to an object:

class Person4:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person4("John", 36)
p1.city = "New York"

print(p1.city)

# Remove properties:
