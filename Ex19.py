""""""Definir una funcio sumar_llista()





def sumar_llista(llista):
    sumar = 0 
    for e in llista:
        sumar += e
        return sumar
    
    def multiplicar_llista(llista):
        multiplicar = 1
        for e in llista:
            multiplicar *= e
            return multiplicar

# programa principal
a = [1, 3, 5]
print("La suma de els elements de la llista {} val {}".format(a, sumar_llista(a)))
print("La multiplicació de els elements de la llista {} val {}".format(a, multiplicar_llista(a)))