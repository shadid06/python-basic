# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Set items are unordered, unchangeable, and do not allow duplicate values.

# Example
# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


# Example
# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)


# Access Items
# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisSet = {"a", "b", "c", "c"}

for i in thisSet:
    print(i)

# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


# Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)


# Change Items
# Once a set is created, you cannot change its items, but you can add new items.
# Add an item to a set, using the add() method:
thisSet.add("z")

print(thisSet)

# To add items from another set into the current set, use the update() method.

thisSet.update(thisset)
print(thisSet)


# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
myList = ["h", "i", "j"]
thisSet.update(myList)
print(thisSet)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

thisSet.remove("apple")
print(thisSet)

thisSet.discard("banana")
print(thisSet)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.

thisSet.pop()
print(thisSet)

# The clear() method empties the set:

thisSet.clear()
print(thisSet)

# The del keyword will delete the set completely:

del thisset
# print(thisset) # this will cause an error because the set is deleted

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# Join Sets
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set4 = set1 | set2
print(set3)
print(set4)

# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"z", "y", "x"}

set4 = set1.union(set2, set3)
set5 = set1 | set2 | set3
print(set4)
print(set5)

# The update() method inserts the items in set2 into set1:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, 'a'}

set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.


# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


# You can use the & operator instead of the intersection() method, and you will get the same result.

set4 = set1 & set2
print(set4)


# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.


# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# The values True and 1 are considered the same value. The same goes for False and 0.

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

# Keep all items from set1 that are not in set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
set4 = set1 - set2
print(set3)
print(set4)

# The difference_update() method will keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)


# he symmetric_difference() method will keep only the elements that are NOT present in both sets.

# Example
# Keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
set4 = set1 ^ set2
print(set3)
print(set4)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

set1.symmetric_difference_update(set2)

print(set1)

# Python frozenset
# frozenset is an immutable version of a set.

# Like sets, it contains unique, unordered, unchangeable elements.

# Unlike sets, elements cannot be added or removed from a frozenset.

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


# Frozenset Methods
# Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

# Method	Shortcut	Description
# copy()	 	Returns a shallow copy
# difference()	-	Returns a new frozenset with the difference
# intersection()	&	Returns a new frozenset with the intersection
# isdisjoint()	 	Returns True if there is NO intersection between two frozensets
# issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another
# issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another
# symmetric_difference()	^	Returns a new frozenset with the symmetric differences
# union()	|	Returns a new frozenset containing the union


# Set Methods
# Python has a set of built-in methods that you can use on sets.

# Method	Shortcut	Description
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns True if NO items of this set is present in another set
# issubset()	<=	Returns True if all items of this set is present in another set
#  	<	Returns True if all items of this set is present in another, larger set
# issuperset()	>=	Returns True if all items of another set is present in this set
#  	>	Returns True if all items of another, smaller set is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others
