# Python Operators
# Operators are used to perform operations on variables and values.

from ast import operator
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)


# Python Arithmetic Operators

# Operator	Name	Example
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y


x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)  # return float
print(x % y)
print(x ** y)
print(x // y)  # return integer

# 13
# 7
# 30
# 3.3333333333333335
# 1
# 1000
# 3

# Assignment Operators

# Operator	Example	Same As
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3
# **=	x **= 3	x = x ** 3
# &=	x &= 3	x = x & 3
# |=	x |= 3	x = x | 3
# ^=	x ^= 3	x = x ^ 3
# >>=	x >>= 3	x = x >> 3
# <<=	x <<= 3	x = x << 3
# :=	print(x := 3)	x = 3
#                       print(x)

# The Ternary Operator
# The ternary operator allows you to assign one value if a condition is true, and another if it is false:

num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)


# Comparison Operators
# Comparison operators are used to compare two values:

# Operator	Name
# ==	Equal
# !=	Not equal
# >	Greater than
# <	Less than
# >=	Greater than or equal to
# <=	Less than or equal to

print(10 == 9)
print(10 != 9)
print(10 > 9)
print(10 < 9)
print(10 >= 9)
print(10 <= 9)

# Chaining Comparison Operators
# Python allows you to chain comparison operators:

x = 5

print(1 < x < 10)

print(1 < x and x < 10)

# Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	Example
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

x = 5

print(x > 0 and x < 10)
print(x < 0 or x < 4)
print(not (x < 5 and x < 10))

# Identity Operators
# Identity operators are used to compare the memory locations of two objects:

# Operator	Description
# is	Returns True if both variables are the same object
# is not	Returns True if both variables are not the same object

x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]

print(x is y)  # False

# Note that this is not the same as ==.
# == checks if two variables are equal in value, but not necessarily the same object.

print(x == y)  # True

# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal


# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	Description	Example
# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

x = ["apple", "banana", "cherry"]

print("banana" in x)

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

# Membership in Strings
# The membership operators also work with strings:

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# Operator	Name	Description	Example
# & 	AND	Sets each bit to 1 if both bits are 1	x & y
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
# ~	NOT	Inverts all the bits	~x
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

# Precedence Order
# The precedence order is described in the table below, starting with the highest precedence at the top:

# Operator	Description
# ()	Parentheses
# **	Exponentiation
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT
# *  /  //  %	Multiplication, division, floor division, and modulus
# +  -	Addition and subtraction
# <<  >>	Bitwise left and right shifts
# &	Bitwise AND
# ^	Bitwise XOR
# |	Bitwise OR
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
# not	Logical NOT
# and	AND
# or	OR
