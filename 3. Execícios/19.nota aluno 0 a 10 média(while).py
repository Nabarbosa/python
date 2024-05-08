import os

SIZE = 2
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

print(f"Média válida: {media}")
