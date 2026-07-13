# Python Functions
# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

def my_function():
    print("my function")


my_function()


# Function Names
# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)
# Example
# Valid function names:

# calculate_sum()
# _private_function()
# myFunction2()


def get_greeting():
    return "Hello from a function"


message = get_greeting()
print(message)


def pass_use():
    pass


# Arguments
# Information can be passed into functions as arguments.

def take_int(num: int):
    """
    This function takes an integer and prints it
    """
    print(num)


take_int(10)


def take_str(name: str) -> None:  # name is a parameter
    """
    This function takes a string and prints it
    """
    print("Hello", name)


take_str("John")


def default_variable(name="friend"):
    print("Hello", name)


default_variable()
default_variable('John')


def send_dict(person):
    print("Name:", person["name"])
    print("Age:", person["age"])


my_person = {"name": "Emil", "age": 25}
send_dict(my_person)


def force_pos_arg(name, /):
    print("Hello", name)


force_pos_arg("Emil")


def force_keyword_arg(*, name):
    print("Hello", name)


force_keyword_arg(name="Emil")


def force_p_k_arg(a, b, /, *, c, d):
    return a + b + c + d


result = force_p_k_arg(5, 10, c=15, d=20)
print(result)


# What is *args?
# The *args parameter allows a function to accept any number of positional arguments.

# Inside the function, args becomes a tuple containing all the passed arguments:

def function_with_args(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)


function_with_args("Emil", "Tobias", "Linus")


def function_with_args_and_other_arg(greeting, *args):
    for name in args:
        print(greeting, name)


function_with_args_and_other_arg("Hello", "Emil", "Tobias", "Linus")


# Scope
# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc():
    x = 300
    print(x)


myfunc()


def function_with_inner_func():
    x = 500

    def inner_func():
        print(x)

    inner_func()


function_with_inner_func()


x = 700


def function_with_global():
    print(x)


function_with_global()

print(x)


def changecase(func):
    def myinner():
        return func().upper()
    return myinner


@changecase
def myfunction():
    return "Hello Sally"


print(myfunction())


def changecase2(func):
    def myinner():
        return func().upper()
    return myinner


@changecase2
def myfunction2():
    return "Hello Sally"


@changecase2
def otherfunction2():
    return "I am speed!"


print(myfunction2())
print(otherfunction2())


# Lambda Functions
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.


def x(a): return a + 10


print(x(5))


def x(a, b): return a * b


print(x(5, 6))


def x(a, b, c): return a + b + c


print(x(5, 6, 7))


def countdown(n):
    if n <= 0:
        print('Done')
    else:
        print(n)
        countdown(n-1)


countdown(10)


def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


print(factorial(5))


# Generators
# Generators are functions that can pause and resume their execution.

# When a generator function is called, it returns a generator object, which is an iterator.

# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


for num in count_up_to(5):
    print(num)
