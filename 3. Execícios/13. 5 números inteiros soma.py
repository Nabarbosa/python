import os

os.system("cls||clear")

soma = 0

for i in range(1, 6):
    numeros = int(input(f"Digite o {i}º número: "))
    soma += numeros
    
print(f"Soma: {soma}")