# Python range
# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

# This set of numbers has its own data type called range.

# range(start, stop, step)

# range(3, 10) returns a sequence of each number from 3 to 9:

# Example
# Create a range of numbers from 3 to 9:

x = range(3, 10)


x = range(3, 10, 2)

# display x:
print(x)

# convert to list to display the content of x:
print(list(x))


# Convert different ranges to lists:

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))
