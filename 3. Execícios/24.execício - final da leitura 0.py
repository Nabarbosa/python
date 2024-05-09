import os
os.system("cls||clear")

somaPares = 0
soma = 0
contador = 0
quantidadePares = 0
quantidadeImpares = 0

print("===== Solicitando dados ===== ")
print("\nO final da leitura acontecerá quando for lido um número zero.\n")

while True:
    numero = int(input("Digite um número: "))

    if numero > 0:
        soma += numero
        contador += 1

        if numero % 2 == 0:
            somaPares += numero
            quantidadePares += 1

        else:
            quantidadeImpares += 1


    if numero == 0:
        break

media = soma / contador

if quantidadePares != 0:
    mediaPares = somaPares / quantidadePares
else:
    mediaPares = 0

print(f"Quantidade de números pares: {quantidadePares}")
print(f"Quantidade de números impares: {quantidadeImpares}")

if quantidadePares != 0:
    print(f"Média dos números pares: {mediaPares}")

print(f"Média dos números inseridos: {media}")
        