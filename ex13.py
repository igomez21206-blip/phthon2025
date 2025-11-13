opcio = int(input("Tria una opció (1 o 2): "))
    1. suma
    2. multiplicació
    3. resta
    4. divisió
    5. sortir
     
a = int(input("Introdueix el primer operand: "))
b = int(input("Introdueix el segon operand: "))
if opcio == 1:
    print("la suma de {} + {} és {}".format(a, b, a + b))
    elif opcio == 2: