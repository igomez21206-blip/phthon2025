def gran_llista(llista):
    if not llista:  # Comprovem si la llista està buida
        return None
    maxim = llista[0]  # Suposem que el primer element és el més gran
    for num in llista:
        if num > maxim:
            maxim = num
    return maxim