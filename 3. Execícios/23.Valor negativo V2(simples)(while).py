import os 
os.system("cls||clear")

contador = 0
soma = 0

while True:
    numeros = int(input("Digite um número: "))

    if numeros >= 0:
        contador += 1
        soma += numeros
    else:
        break

media = soma / contador

print(f"Média: {media}")