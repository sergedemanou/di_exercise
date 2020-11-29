# Exercise 1: Cats
# Consider this class
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Instantiate 3 Cat objects using our class
# Create a function that finds the oldest cat and returns the cat
# Print out: “The oldest cat is , and is years old.” using the method previously created

# 1.
# class Cat():
#
#      def __init__(self, c_name, c_age):
#          self.name = c_name
#          self.age = c_age
#
# cat1 = Cat("medor",3)
# cat2 = Cat("michat", 5)
# cat3 = Cat("minou",1)
#
# def catInfo():
#     if cat1.age>cat2.age and cat1.age>cat3.age:
#         print("The oldest cat is {} and is {} years old".format(cat1.name, cat1.age))
#     elif cat2.age>cat1.age and cat2.age>cat3.age:
#         print("The oldest cat is {} and is {} years old".format(cat2.name, cat2.age))
#     else : print("The oldest cat is {} and  is {} years old".format(cat3.name, cat3.age))
#
# catInfo()
#

#                                  Exercise 2 : Dogs
# Create a class Dog.
# In this class, create a method __init__, that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method named bark that prints “ goes woof!”
# Create a method jump that prints the following “ jumps cm high!” where x is the height*2.
# Outside of the class, create an object davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog by calling the methods.
# Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog by calling the methods.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def bark(self):
#         print("goes woof !")
#
#
#     def jump(self):
#          print("jumps {} cm high".format(self.height*2))
#
#
#
# davids_dog = Dog("Rex",50)
# print('the davids dog is {} and it jumps {} cm'.format(davids_dog.name, davids_dog.height))
#
# sarahs_dog = Dog("Teacup",20)
# print('the sarahs_dog is {} and it jumps {} cm'.format(sarahs_dog.name, sarahs_dog.height))
#
# if sarahs_dog.height>davids_dog.height:
#     print("{} is bigger than {} ".format(sarahs_dog.name, davids_dog.name))
# else:
#     print("{} is bigger than {} ".format(davids_dog.name, sarahs_dog.name))


#                            Exercise 3 : Who’s The Song Producer ?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics(a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the method sing_me_a_song. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for i in self.lyrics:
#             print(i)
#
#
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# Create a class Zoo
# In this class create a method __init__ that takes one parameter: zoo_name
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list, only if the new_animal isn’t already in the list.
# Create a method get_animals that prints all the of animals in the zoo.
# Create a method sell_animal that takes one parameter animal_sold. This method removes the animal from the list, only if he was already in the list.
# Create a method sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
# Create a method get_groups that prints the animal/animals inside each group.
# Create an object ramat_gan_safari and call all the methods.
# Tip: for each method, the argument should be the answer of the zoo keeper.
# Example
#
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)


class Dog:
    def __init__(self, dogname, weight, height):
        self.name = dogname
        self.weight = weight
        self.height = height

    def bark(self):
        print("the name of my dog is {}, it is {} kg and it's height is {} cm".format(self.name, self.weight, self.height))


d = Dog("Rex", 10, 25)
d.bark()
