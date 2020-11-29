# Exercise 1 : Pets
# Consider this code
#
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
# Add another cat breed
# Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
# Instantiate the Pet class with all your cats. Use the variable my_pets
# Output all of the cats walking using the my_pets instance


# class Pets():
#     animals = []
#
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
#
# class Bengal(Cat):
#
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Chartreux(Cat):
#
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Persan(Cat):
#
#     def sing(self, sounds):
#         return f'{sounds}'
#
# cat1 = Bengal ('minou', 4)
# cat2 = Chartreux ('michat', 3)
# cat3 = Persan ('chati', 2)
#
# my_cats = [cat1, cat2, cat3]
#
# my_pets = Pets(my_cats)
#
# my_pets.walk()
#

                        # Exercise 2 : Dogs
# Create a class named Dog with the attributes name, age, weight
# Implement the following methods for the class:
# bark: returns a string of “ barks”.
# run_speed: returns the dogs running speed (weight/age *10).
# fight : gets parameter of other_dog, returns string of which dog won the fight between them, whichever has a higher run_speedweight* should win.
# Create 3 dogs and use some of your methods

class Dogs():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight


    def bark(self):
        print('barks')

    def run_speed(self):
        print('{} is running at {} km/h'.format(self.name, self.weight/self.age*10 ))

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            print("{} is the winner ".format(self.name))
        else:
            print("{} is the winner".format(other_dog.name))


dog1 = Dogs("Boss", 3, 80)
dog2 = Dogs("Miky", 4, 90)
dog3 = Dogs("Rex", 5, 110)

# dog1.bark()
# dog1.run_speed()
# dog2.run_speed()
# dog3.run_speed()




                             # Exercise 2 : Dogs Domesticated
# Create a new python file and import your Dog class from the previous exercise.
# Create a class named PetDog that inherits from Dog.
# Add the attribute trained (boolean) to the PetDog class, should always start False
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
# play: gets parameter of any amount of other dogs (look up args) and prints “the dogs: dog_names play together” each of the dogs that plays has their trained boolean switched to False
# do_a_trick: will print one of the following sentences randomly ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
# “dog_name does a barrel roll”
# “dog_name stands on their back legs”
# “dog_name shakes your hand”
# “dog_name plays dead”

