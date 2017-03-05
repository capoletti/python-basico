"""
Listas - colchetes
"""

integer_list = [1,2,3]
heterogenous_list = ["string", 0.1, True]
multiple_list = [integer_list, heterogenous_list, []]

#tamanho de lista
print len(integer_list)

#somar valores de uma lista
print sum(integer_list)

#inicializa a lista com dez elementos
x = range(10)
print "lista: " + str(x)

#elementos
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]

print str(zero) + " - " + str(one) + " - " + str(nine) + " - " + str(eight)

#alterando valores
x[0] = -1
print "lista nova: " + str(x)

#repartindo listas
first_three = x[:3]
print "first_three: " + str(first_three)

three_to_end = x[3:]
print "three_to_end: " + str(three_to_end)

one_to_four = x[1:5]
print "one_to_four: " + str(one_to_four)

last_three = x[-3:]
print "last_three: " + str(last_three)

copy_x = x[:]
print "copy_x: " + str(copy_x)

#procurar elemento na lista
print "Existe 1 na lista 1, 2, 3: " + str(1 in [1,2.3])
print "Existe 0 na lista 1, 2, 3: " + str(0 in [1,2.3])

#concatenar listas
l1 = [1,2,3]
print "l1: " + str(l1)

l1.extend([4,5,6])
print "l1 + ext: " + str(l1)

l11 = [1,2,3]
l12 = l1 + [4,5,6]
print "l12: " + str(l12)

lx = [1,2,3]
lx.append(0)
print "lx: " + str(lx)

#segregar lista
s1, s2 = [1,2]
print "s1: " + str(s1)
print "s2: " + str(s2)

_, s3 = [1,2]
print "s3: " + str(s3)