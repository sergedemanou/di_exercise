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
my_list = [x*3 for x in range(3, 31)]
print(my_list)