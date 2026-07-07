# List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
print(thislist)

print(len(thislist))  # length of the list

# A list can contain different data types:

list1 = ["abc", 34, True, 40, "male"]

print(type(list1))  # type of the list

# Example
# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry"))
print(thislist)


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access Items
# List items are indexed and you can access them by referring to the index number:


# Example
# Get the first item:

thislist = ["apple", "banana", "cherry"]

print(thislist[0])  # apple

# Get the second item:

print(thislist[1])  # banana

# Get the last item:

print(thislist[-1])  # cherry

# Get the second last item:

print(thislist[-2])  # banana

# Get the third last item:

print(thislist[-3])  # apple

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]  # 1-2 index change
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]  # 1-2 index replace by one item
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# Remove Specified Index
# The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # remove the item at index 1
print(thislist)
# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()  # remove the last item
print(thislist)

# The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[1]  # remove the item at index 1
print(thislist)
# The del keyword can also delete the list completely:

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)

# The clear() method empties the list.

# The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# Loop Through a List

# You can loop through the list items by using a for loop:

theList = ["a", "b", "c"]
for item in theList:
    print(item)


# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

theList = ["d", "e", "f"]
for i in range(len(theList)):
    print(theList[i])


# Using a While Loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

newList = [5, 6, 7, 8, 8, 10]
i = int(0)
while i < len(newList):
    print(newList[i])
    i += 1

# A short hand for loop that will print all items in a list:

shorthandList = [5, 6, 7, 8, 8, 10]
[print(i) for i in shorthandList]


# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ['aam', 'jaam', 'kathal']
bucket = []
for x in fruits:
    if 'm' in x:
        bucket.append(x)

print(bucket)

shortBucket = [x for x in fruits if 'a' in x]

print(shortBucket)

newFruits = [x for x in fruits]
print(newFruits)

newList = [x for x in range(10)]
print(newList)

newlist = [x for x in range(10) if x < 5]
print(newlist)

fruitsUpperCase = [x.upper() for x in fruits]
print(fruitsUpperCase)

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)


# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Make a copy of a list with the : operator:

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append list2 into list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
