    #Exercise 1
#Print the following output in one line of code:

a = "Hello world " * 4
print(a)

#Exercise 2 : Some Math
#Calculate the result of: (99^3) * 8

b = (99**3) * 8
print(b)

# Exercise 3 : What Is The Output ?
# Predict the output of the following code snippets:
# >>> 5 < 3 False
# >>> 3 == 3 True
# >>> 3 == "3" False
# >>> "3" > 3 False
# >>> "Hello" == "hello" False

# Exercise 4 : Your Computer Brand
# Create a variable called computer_brand that contains the brand of your computer.
# Insert and print the above variable in a sentence,like "I have a razer computer".

computer_brand = "Dell"
print('I have a {} computer'.format(computer_brand))

# Exercise 5: Your Information
# Create a variable called name, and give it your name as a value (text)
# Create a variable called age, and give it your age as a value (number)
# Create a variable called shoe_size, and give it your shoe size as a value
# Create a variable called info. Its value should be an interesting sentence about yourself, including your name, age, and shoe size. Use the variables you created earlier.
# Have your code print the info message.
# Run your code

name = "Serge"
age = 30
shoe_size = 43
info = "My name is {} , i'm {} years old and i shoe {} .".format(name, age, shoe_size)
print(info)

# Exercise 6: Odd Or Even
# Write a script that asks the user for a number and determines whether this number is odd or even.

number = input("Enter Integer")
if int(number) % 2 == 0:
    print("{} is even.".format(number))
else:
    print("{} is odd.".format(number))

# Exercise 7 : What’s Your Name ?
# Write a script that asks the user for his name and determines whether or not you have the same name, print out a funny message based on the outcome

phrase = input("please enter your name")
if "serge" in phrase :
    print("wow we have the same name")
else:
    print("input another name please")

    # Exercise
    # 8: Tall
    # Enough
    # To
    # Ride
    # A
    # Roller
    # Coaster
    # Write
    # a
    # script
    # that
    # will
    # ask
    # the
    # user
    # for their height in inches, print a message if they can ride a roller coaster or not based on if they are taller than 145cm
    # Please
    # note
    # that
    # the
    # input is in inches and you’re
    # calculating
    # vs
    # cm, you’ll
    # need
    # to
    # convert
    # your
    # data
    # accordingly


a = int(input("what\'s your height in inches please?"))
b: int = 57.0866
if a > b:
    print("you can ride a roller coaster")
else:
    print(" sorry you can't ride a roller coaster")
