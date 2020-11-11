
for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0:
        print('Fizz')
        continue
    elif fizzbuzz % 5 == 0:
        print('Buzz')
        continue
    elif fizzbuzz % 5 == 0 and fizzbuzz % 3 == 0:
        print("FizzBuzz")
        continue
    print(fizzbuzz)

nombre1 = 5
nombre2 = 6
q = nombre2 // nombre1
print('le resultat est {}'.format(q))