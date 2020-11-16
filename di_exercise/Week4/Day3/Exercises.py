             # Exercise 1 :
# Convert Lists Into Dictionaries
# # Convert the two following lists, into dictionaries.
# # Hint: Use the zip method
# # keys = ['Ten', 'Twenty', 'Thirty']
# # values = [10, 20, 30]
# # Expected output:
# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# x = dict(zip(keys, values))
# print(x)

                     # Exercise 2 : Cinemax #2
# “Continuation of Exercise Cinemax of Week4Day2 XP”
#
# A movie theater charges different ticket prices depending on a person’s age. if a person is under the age of 3,
# the ticket is reef if they are between 3 and 12, the ticket is $10; and if they are over age 12,
# the ticket is $15 . Here is the object you will work with : family = {"rick": 43, 'beth': 13,
# 'morty': 5, 'summer': 8} Using a for loop, the dictionary above, and the instructions, print out how
# much each family member will need to pay alongside their name After the loop print out the family’s
# total cost for the movies Bonus: let the user input the names and ages instead of using the provided
# family variable (Hint: ask the user for names and ages and add them into a family dictionary that is
# initially empty)

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# age = int(input("please enter your age :"))
# if age<3 :
#     print('the ticket is free')
# elif 3< age <12 :
#     print('the ticket is $10')
# else :
#     print('the ticket is $15')
#
# for x in family(keys, values):


                            # Exercise 3: Zara
# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: France -> blue, Spain -> red, US -> pink, green
# Create a dictionary called brand, and translate the information above into keys and values.
# Change the number of stores to 2.
# Print a sentence that explains who the clients of Zara are.
# Add a key called country_creation with a value of Spain to brand
# If the key international_competitors is in the dictionary, add the store Desigual.
# Delete the information about the date of creation.
# Print the last international competitor.
# Print in a sentence, the major clothes’ colors in the US.
# Print the amount of key value pairs (length of the dictionary).
# Print only the keys of the dictionary.
# Create another dictionary called more_on_zara with the following information:
# creation_date: 1975
# number_stores: 10 000
# Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# Print the value of the key number_stores. What just happened ?

brand = {
    "name": "Zara",
    "creation_date": "1975",
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color":{
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"],
    }
}
brand["number_stores"] = 2
print("The clients of Zara are {}, {}, and {}")



