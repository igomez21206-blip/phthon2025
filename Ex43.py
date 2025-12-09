# Programa per imprimir 5 vegades la sèrie de números de l'1 al 15

# Nombre de repeticions
repeticions = 5

# Sèrie de números
inici = 1
final = 15

# Bucle principal per repetir la sèrie
for rep in range(1, repeticions + 1):
    print(f"Sèrie {rep}: ", end="")
    
    # Imprimir números de 1 a 15
    for num in range(inici, final + 1):
        print(num, end=" ")
    
    print()  # Salta a la següent línia després de cada sèrie
