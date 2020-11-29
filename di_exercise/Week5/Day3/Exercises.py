# Exercise 1 : Built-In Functions
# Python has many built-in functions, and if you do not know how to use it, you can read document online.
# But Python has a built-in document function for every built-in functions.
#
# Write a program to print some Python built-in functions documents, such as abs(), int(), raw_input().
# And add documentation for your own function
def abs__doc__():
    pass

def int__doc__():
    pass

def raw_input__doc__():
    pass


print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


# Exercise 2: Currencies
# Recreate these results
# Hint : When you add 2 currencies, if they don’t have the same label raise an error
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c4 = Currency('shekel', 1)
# >>> c3 = Currency('shekel', 10)
# >>> str(c1)
# '5 dollars'
# >>> int(c1)
# 5
# >>> repr(c1)
# '5 dollars'
# >>> c1 + 5
# 10
# >>> c1 + c2
# 15
# >>> c1
# 5 dollars
# >>> c1 += 5
# >>> c1
# 10 dollars
# >>> c1 += c2
# >>> c1
# 20 dollars
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
# Look at the lesson on Datetime Module for the exercises 3,4,5