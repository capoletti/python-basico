"""
Estruturas de controle 
"""

#loop while
x = 0
print "while 0 - 4"
while x < 5:
    print x
    x += 1

#loop for
print "for 0 - 10"
for x in range(10):
    print x
    if x == 3:
        print "continue"
        continue
    if x == 5:
        print "break"
        break

#veracidade
x = None
print "Igual a None: " + str(x is None)

#funcoes all e any
print "all - verdadeiro: " + str( all( [True, 1, {3}] ) )
print "all - falso: " + str( all( [True, 1, {}] ) )
print "any - verdadeiro: " + str( any( [True, 1, {}] ) )
print "all - []: " + str( all( [] ) ) #sem elemento falso
print "any - []: " + str( any( [] ) ) #sem elemento verdadeiro