from functools import reduce

def Passar_a_Numero(llista):
    return reduce(lambda x, y: x * 10 + y, llista)