"""
Ordenacao em listagem
"""

#ordenar nova lista
x = [4,1,2,3]
y = sorted(x)

print "Lista X: " + str(x)
print "Lista Y: " + str(y)

#ordenar a propria lista2
x.sort()

print "Lista ordem X: " + str(x)

#transformando listas
numbers = range(5)
squares = [x * x for x in numbers]
print "numbers: " + str(numbers)
print "squares: " + str(squares)

squares_dict = {x : x * x for x in numbers}
print "squares_dict: " + str(squares_dict)

pairs = [(x,y)
        for x in range(10)
        for y in range(2)]

print "pairs: " + str(pairs)
