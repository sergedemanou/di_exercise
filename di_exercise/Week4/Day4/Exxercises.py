#                     Exercise 1 : What Are You Learning ?
# Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
# Call the function, and make sure the message displays correctly.

# def display_message():
#     print ("i'm learning web development")
# display_message()

#                        Exercise 2: What’s Your Favorite Book ?
# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, making sure to include a book title as an argument in the function call.

# def favorite_book(title):
#     print("One of my favorite book is " + title)
# favorite_book("Alice in wonderland")

                     # Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

# def describe_city(city, country):
#     print(city + " is in " + country)
# describe_city("Reykjavik", "Iceland")

# def describe_city(city, country="Cameroun"):
#     print(city + " is in " + country)
# describe_city("Reykjavik")
# describe_city("Yaoundé")
# describe_city("Douala")


                      # Exercise 4 : Let’s Create Some Personalized Shirts !
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# def make_shirt(size, text):
#     print("this shirt is "+ size + " and " + text)
# make_shirt("xxl", "I love Nike")
#
# def make_shirt(text, size="large"):
#     print("I wear a shirt size " + size + " and " + text )
# make_shirt("I love Python")
#
# def make_shirt(size, text= "I love Python"):
#     print("I wear a " + size + " and " + text)
# make_shirt("large shirt")
# make_shirt("medium shirt")
# def get_formatted_name(size, text):
#     fulltext = "I wear shirt " + size + " and " + text
#     return fulltext
# allT = get_formatted_name("xxl", 'i love addidas')
# allT = get_formatted_name("xl", 'i love puma')


                  # Exercise 5 : Magicians …
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.

# 1.  2.
magicians_names = ["Paul", "Pierre", "Joseph", "André"]
def show_magicians(magicians):
    for i in magicians:
        print(i)

# 3.

def make_great(list):
    great_magicians = ["the Great " + name for name in list]
    return great_magicians
new_magicians = make_great(magicians_names)
show_magicians(new_magicians)