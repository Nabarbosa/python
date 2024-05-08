"""
import os

os.system("cls||clear")

soma = 0

for i in range(4):
    numero = int(input(f"Digite a {i+1}ª nota: "))

    soma += numero

media = soma / 4

print(f"==== Exibindo resultados ====")
print(f"Média: {media}")

"""

import os

os.system("cls||clear")

size = 3
soma = 0

for i in range(size):
    numero = int(input(f"Digite a {i+1}ª nota: "))

    soma += numero

media = soma / size

print(f"==== Exibindo resultados ====")

print(f"=== Média: {media}")

if media >= 7:
    print(f"=== Aprovado! ===")
elif media < 4:
    print(f"=== Reprovado! ===")
else:
    print(f"=== Recuperação! ===")



