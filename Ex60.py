def es_primer(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primers = []

for num in range(1, 101):
    if es_primer(num):
        primers.append(num)

print("Números primers entre 1 i 100:")
print(primers)
print(f"Total de números primers: {len(primers)}")
