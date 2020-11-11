#       Exercise 1 : Favorite Numbers
# Create a set called my_fav_numbers with your favorites numbers.
# Add two new numbers to it.
# Remove the last one.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

# my_fav_numbers = {2, 6, 3, 8}
# set.add(1)
# set.add(0)
# set.remove(8)
# friend_fav_numbers = {12, 30}
# our_fav_numbers = my_fav_numbers|friend_fav_numbers

#               Exercise 2: Tuple
# Given a tuple with integers is it possible to add more integers to the tuple?

# No, Tuples are immutable lists, it means items can’t be changed

#             Exercise 3: Print A Range Of Numbers
# Use a for loop to print the numbers from 1 to 20, inclusive.

# for i in range (1, 21):
#     print("{}".format(i))


#                Exercise 4: Floats
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way of generating a sequence of floats?
# Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.

# a = list(range(3, 11))
# for i in a:
#     a = i*0.5
#     print(a)

#                         Exercise 5: Shopping List
# Consider this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Put “Kiwi” at the end of the list.
# Add “Apples” at the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

# basket.pop(0)
# basket.pop()
# basket.append('Kiwi')
# basket.insert(0, "Apples")
# x = basket.count('Apples')
# print('x')
# basket.clear()
# print('basket')
#
#                        Exercise 6 : Loop
# Write a while loop that will keep asking the user for input until the input is the same as your name.

# name = input('enter the right name')
# while name != "serge":
#     name = input('enter the right name')

#                              Exercise 7
# Given a list, use a while loop to print out every element which has an even index.
# list = [i for i in range(10)]
# index = 0
# while index < len(list):
#     print(list[index])
#     index = index+2


                          # Exercise 8
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
# array = []
# for x in range(3, 31):
#     if x%3 == 0:
#      print(x)


#                              # Exercise 9
# # Use a for loop to find numbers between 1500 and 2700, which are divisible by 7 and multiples of 5.
# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#      print (x)



                # Exercise 12: Cinemax
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15 .
# Apply it to a family, ask the user what the age of each of the people that want a ticket is.
# Store the total cost of all the tickets for this group and print it out.
# A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
# Write a program that ask every user their age, and then tell them which one can see the movie.
# Tip: Try to add the allowed ones to a list.

age = int(input("please enter your age :"))
if age<3 :
    print('the ticket is free')
elif 3< age <12 :
    print('the ticket is $10')
else :
    print('the ticket is $15')