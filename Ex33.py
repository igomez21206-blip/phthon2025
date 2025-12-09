def nums_que_comencen_per(noms, lletra="a"):
    comptador = 0
    lletra = lletra.lower()
    
    for nom in noms:
        if nom.lower().startswith(lletra):
            comptador += 1
    
    return comptador