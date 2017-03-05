"""
Conjuntos de dados - set - parenteses
"""

s = set()

#adiciona os elementos, por�m apenas uma unica vez
s.add(1)
print "conjunto add(1): " + str(s)

s.add(2)
print "conjunto add(2): " + str(s)

s.add(2)
print "conjunto add(2): " + str(s)

#verificando a existencia
#conjuntos s�o muito rapidos para verificar a existencia (in)
print "conjunto tamanho: " + str(len(s))
print "conjunto existe 2: " + str(2 in s)
print "conjunto existe 3: " + str(3 in s)

#listas distintas
item_list = [1,2,3,1,2,3]
item_set = set(item_list)
dist_item_list = list(item_set)

print "lista: " + str(item_list)
print "conjunto: " + str(item_set)
print "lista dist: " + str(dist_item_list)

