                        # Exercise
# Write a program that prints the numbers from 1 to 100 inclusive
#
# But for multiples of three print “Fizz” instead of the number
#
# For the multiples of five print “Buzz”.
#
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

for i in range(1, 101):
    if i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else: print(i)

# nombre1 = 5
# nombre2 = 6
# q = nombre2 // nombre1
# print('le resultat est {}'.format(q))
