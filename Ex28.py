def filtrar_paraules(llista_paraules, x):
    """
    Retorna una nova llista amb les paraules de llista_paraules
    que tinguin més de x caràcters.
    
    Paràmetres:
    llista_paraules : list
        Llista de paraules a filtrar.
    x : int
        Nombre mínim de caràcters + 1 que ha de tenir la paraula.
    
    Retorn:
    list
        Llista de paraules amb més de x caràcters.
    """
    return [paraula for paraula in llista_paraules if len(paraula) > x]
