#classe de modelo
class Conjunto:
    """conjunto"""

    def __init__(self, values=None):
        s1 = set()
        s2 = set([1,2,2,3])
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def add(self,value):
        self.dict[value] = True
    
    def contains(self,value):
        return value in self.dict

#acessando a clase conjunto
s = Conjunto([1,2,3])
s.add(4)
print s.contains(3)
