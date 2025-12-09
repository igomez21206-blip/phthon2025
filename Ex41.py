# Programa per calcular la suma dels quadrats de nombres separats de 4 en 4

# Demanar un número menor de 100
while True:
    try:
        num = int(input("Introdueix un número menor de 100: "))
        if num < 100:
            break
        else:
            print("El número ha de ser menor de 100.")
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")

# Inicialitzar la suma
suma_quadrats = 0

print("\nCalculant els quadrats dels números separats de 4 en 4:")

# Recórrer els números de num cap a 0 amb passos de 4
for i in range(num, 0, -4):
    quadrat = i ** 2
    suma_quadrats += quadrat
    print(f"{i}^2 = {quadrat}")

# Mostrar la suma total
print("\nSuma total dels quadrats:", suma_quadrats)