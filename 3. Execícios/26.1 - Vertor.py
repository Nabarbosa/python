import os
os.system("cls || clear")

# Criando uma constante.
SIZE = 3

notas = []

for i in range(SIZE):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

media = sum(notas)/ SIZE

print(f"\n=== Exibindo notas ===")

#ForEach
for nota in notas:
    print(f"Notas : {nota}")

print(f"\n=== Exibindo média ===")
print(f"Média : {media}")