"""
Tuplas: listas imutaveis  
"""

#tuplas nao podem ser modificadas
list_1 = [1,2]
tuple_1 = (1,2)
tuple_2 = 3, 4

try:
    list_1[1] = 3
    tuple_1[1] = 3
except TypeError:
    print "erro ao modificar uma tupla"

print "lista: " + str(list_1)
print "tupla: " + str(tuple_1)

#tuplas sao eficazes para retornar multiplos valores
def sum_and_product(v1,v2):
    return (v1+v2), (v1*v2)

r1, r2 = sum_and_product(5,10)
print "r1: " + str(r1)
print "r2: " + str(r2)


