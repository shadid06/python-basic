# Placeholders and Modifiers
# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {95:.2f} dollars"
print(txt)


txt = f"The price is {20 * 59} dollars"
print(txt)


price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)


def myconverter(x):
    return x * 0.3048


txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)


# Formatting Types
# :<		Left aligns the result (within the available space)
# :>		Right aligns the result (within the available space)
# :^		Center aligns the result (within the available space)
# :=		Places the sign to the left most position
# :+		Use a plus sign to indicate if the result is positive or negative
# :-		Use a minus sign for negative values only
# : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,		Use a comma as a thousand separator
# :_		Use a underscore as a thousand separator
# :b		Binary format
# :c		Converts the value into the corresponding Unicode character
# :d		Decimal format
# :e		Scientific format, with a lower case e
# :E		Scientific format, with an upper case E
# :f		Fix point number format
# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g		General format
# :G		General format (using a upper case E for scientific notations)
# :o		Octal format
# :x		Hex format, lower case
# :X		Hex format, upper case
# :n		Number format
# :%		Percentage format


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
