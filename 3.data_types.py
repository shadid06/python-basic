# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = 5
print(type(x))


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

string = str("hello")
integer = int(20)
float_type = float(3.3)
complex_type = complex(1j)
list_type = list(("a", "b", "c"))  # mutable
tuple_type = tuple(("a", "b", "c"))  # immutable
print(tuple_type)
range_type = range(6)
print(range_type)
dict_type = dict({"brand": "Ford", "model": "Mustang",
                 "year": 1964})  # mapping aka object
print(dict_type)
set_type = set(("apple", "banana", "cherry", "apple", "banana"))  # mutable
print(set_type)
frozenset_type = frozenset(
    ("apple", "banana", "cherry", "apple", "banana"))  # immutable
print(frozenset_type)
bool_type = bool(10)
print(bool_type)
bytes_type = bytes(5)
print(type(bytes_type))
bytearray_type = bytearray(5)
print(type(bytearray_type))
memoryview_type = memoryview(bytes(5))
print(type(memoryview_type))
none_type = None  # it is actually null
print(type(none_type))
