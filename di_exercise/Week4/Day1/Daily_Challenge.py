# Daily Challenge : Build Up A String
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”
# If it’s more than 10 characters, print a message which states “string too long”
# Then, print the first and last characters of the given text
# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
# Example:
# The user enters “Hello Word”
# Then, you have to construct the string character by character
# H
# He
# Hel
# … etc
# Hello World
# Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
# Example:
# Hlrolelwod

# 1.
# import random
# print("enter a string please")
# str = input()
# if (len(str)==10):
#     print(str)
# elif (len(str)<10) :
#     print("string is not long enough")
# else:
#     print("string too long")

# 3.



# 2.
# first_caracter = str[0]
#
# last_caracter = str[-1]
# print(first_caracter, last_caracter)

# 4.
import random
a= "Bonjour Serge"
a = list(a)
random.shuffle(a)
a=''.join(a)
print(a)