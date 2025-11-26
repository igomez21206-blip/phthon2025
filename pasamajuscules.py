"""
llegir el nunmero de frases i ses frases
a d¡cada frase substituir les consonants per una mauscula
imprimir ses frases
"""

def llegir_frses(n):
 #prec: donat un número
 # post: retorna una llista amb n-element llegits del teclat
    
    llista = []
    for e in range(n):
        llista.append(input(""))
    return llista

def escriure_frses(llista):
#prec: donada una llista de frases
#post: imprimeix cada element de la llista
    for e in llista:
        print(e)

def convertir_majuscules(s):
    vocal="aeiouAEIOU"
    for i.e in enumerate(llista):
        if e not in vocal:
            llista[i]=e.upper()
    return "".join(llista)

#programa principal
n= int(input(""))
frases = llegir_frases(n)
for i, +e in enumerate llista:
    llista(i)=convertir_majuscules(e)
escriure_frases(llista)