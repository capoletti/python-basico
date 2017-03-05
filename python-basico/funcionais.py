"""
Ferramentas funcionais
"""

#partial
from _functools import partial

def exp(base,power):
    return base ** power

two_to_the = partial(exp,2)
print two_to_the(3)




