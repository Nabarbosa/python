import os

os.system("cls||clear")

quantPares = 0
quantImpares = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
   
    if numero % 2 == 0:
        quantPares += 1
    else:
        quantImpares += 1

print(f"Quantidade de pares: {quantPares}")
print(f"Quantidade de impares: {quantImpares}")
