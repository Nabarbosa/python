import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 6
numeros = []
pares = 0
impares = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite {i + 1}º número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

os.system("cls || clear")

print(f"\n=== Exibindo resultados ===\n")

for i, numero in enumerate(numeros):
    print(f"{i +1}º Número informado: {numero}")

print(f"\n== Quantidade de números ==\n")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números impares: {impares}")