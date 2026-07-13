# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.
import json
# Convert from JSON to Python:
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON:


# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null
