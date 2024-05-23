import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
numeros = []

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}ª número: "))
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)

print(f"\nNúmeros informado pelo usuário:")

for i, numero in enumerate(numeros):
    print(f"{i + 1}º número : {numero}")


print(f"\n === Maior e Menor número === ")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
