def eliminarcapicua(llista):
    return llista[1:-1]  # retorna la llista sense el primer i últim element

# Prova
fruits = ["poma", "plàtan", "cirera", "mango", "pera"]
print("Original:", fruits)
print("Modificada:", eliminarcapicua(fruits))