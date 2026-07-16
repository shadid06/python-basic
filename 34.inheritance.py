class Person:
    def __init__(self, fname: str, lname: str):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)


x = Person("John", "Doe")
x.print_name()


# class Student(Person):
#     pass


# x = Student("Mike", "Olsen")
# x.print_name()


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2026


x = Student("John", "Doe")

print(x.graduationyear)
