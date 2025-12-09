def paraula_mes_llarga(llista_paraules):
    # Comprovem si la llista no està buida
    if not llista_paraules:
        return None  # Retorna None si la llista està buida
    
    # Inicialitzem amb la primera paraula
    paraula_mes_llarga = llista_paraules[0]
    
    # Recorrem la llista per trobar la paraula més llarga
    for paraula in llista_paraules:
        if len(paraula) > len(paraula_mes_llarga):
            paraula_mes_llarga = paraula
    
    return paraula_mes_llarga