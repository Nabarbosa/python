import os

SIZE = 3
soma = 0

os.system("cls||clear")

for i in range(SIZE):
    while True: 
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida. \nA nota deve estar entre 0 e 10. \nPor favor tente novamente.")
        else:
            soma += nota
            break    

media = soma / SIZE

print(f"\n=== Exibindo resultados ===")
print(f"\nMédia válida: {media}")

if media >= 7:
    print(f"\n=== Aprovado! ===")
elif media < 5:
    print(f"\n=== Reprovado! ===")
else:
    print(f"\n=== Recuperação! ===")

"""
Outra maneira de fazer:

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"Situação do aluno: {resultado})

""" 