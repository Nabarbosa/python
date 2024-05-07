import os

os.system("cls||clear")

soma = 0

for i in range(3):
    numero = int(input(f"Digite o {i+1}º nota: "))

    soma += numero

media = soma / 3

if media >= 7:
    print(f"=== Aprovado ===")
elif media < 4:
    print(f"=== Reprovado ===")
else:
    print(f"=== Recuperação ===")

print(f"==== Exeibindo resultados ====")
print(f"Média das notas: {media}")

"""Considere que para aprovação, deve-se obter média
maior ou igual a 7, para ser reprovado, a média deve
ser menor que 4. 
"""