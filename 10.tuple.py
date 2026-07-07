# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

createTuple = tuple(("a", "b", "c"))
print(createTuple)
print(type(createTuple))


# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# Example
# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple Items - Data Types
# Tuple items can be of any data type:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")

# Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

fruitTuple = ("banana", "apple", "cherry", "orange", "kiwi", "melon", "mango")
if "apple" in fruitTuple:
    print("apple is in the tuple")
else:
    print("apple is not in the tuple")


# Python - Update Tuples

# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# But there are some workarounds.

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = tuple((1, 2, 3, 4, 5))
y = list(x)
y[0] = 0
x = tuple(y)
print(x)


# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)


# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)


# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # this will raise an error because the tuple no longer exists

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# Packing a tuple:

fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# Example
# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk
# If the number of variables is less than the number of values, you can add an asterisk to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Using Asterisk in the middle
# If the asterisk is added to another variable name, Python will assign values to that variable according to the number of remaining values:

# Example
# Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# What if the asterisk is not last?
# If the asterisk is not the last variable in the unpacking, Python will assign values to the variable until the number of values left matches the number of variables left:


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

thistuple = ('a', 'b', 'c', 'd')
for x in thistuple:
    print(x)


# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

thistuple1 = ('n', 'o', 'v', 'e', 'm', 'b', 'e', 'r')

for i in range(len(thistuple1)):
    print(thistuple1[i])
