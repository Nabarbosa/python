import os
os.system("cls || clear")

numeros = []

while True:
    numero = int(input("Digite o número: "))
    if numero == 0:
        break
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)

print(f"\nNúmeros informado pelo usuário:")

for i, numero in enumerate(numeros):
    print(f"{i + 1}º número : {numero}")


print(f"\n === Maior e Menor número === ")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")