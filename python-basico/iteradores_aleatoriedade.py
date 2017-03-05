"""
Iteradores e numeros aleatorios
"""
import random

#lazy range
def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in lazy_range(10):
    print str(i)

#numeros randomicos
four_random = [random.random() for _ in range(4)]

print four_random

random.seed(5)

print "seed: " + str(random.random())

print "randrange 0-10: " + str(random.randrange(10))
print "randrange 3-6: " + str(random.randrange(3,6))

#random escolha
print "" + str(random.choice(["nome 1","nome 2","nome 3","nome 4"]))

