import os

os.system("cls||clear")

soma = 0

for i in range(4):
    numero = int(input(f"Digite o {i+1}º número: "))

    soma += numero

media = soma / 4

print(f"==== Exeibindo resultados ====")
print(f"Média das notas: {media}")