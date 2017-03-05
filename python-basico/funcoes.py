"""
Funcoes
"""

#funcaoo simples
def double(x):
    return x * 2

#recepcionar uma funcao como parametro de entrada
def apply_to_five(f):
    return f(5)

#funcao com lambda
second_double = lambda x: 2 * x

#executar as funcoes
my_double = double
y = apply_to_five(my_double)

print "o dobro de cinco: " + str(y)

print "o dobro de tres: " + str(double(3))

print "o dobro de quatro: " + str(second_double(4))