class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


mycar = Car("Ford", "Mustang")
myboat = Boat("Ibiza", "Touring 24")
myplane = Plane("Boeing", "747")

for i in (mycar, myboat, myplane):

    i.move()
