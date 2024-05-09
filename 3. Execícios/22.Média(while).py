import os

os.system("cls||clear")

contadorNotas = 0
soma = 0

resposta = input(" S - Inserir mais uma nota. \n P - Ver quantas notas foram inseridas. \n N - Calcular a média das notas informadas.")

while True:
    nota = float(input("\n Digite a nota: "))
    resposta = input("\n Escolha uma opção:")

    if resposta == "s":
        contadorNotas += 1
        soma += nota

    elif resposta == "p":
        contadorNotas += 1
        print(f"Contador: {contadorNotas}")

    elif resposta == "n":
        media = soma / contadorNotas
        print(f"Média: {media}")
        break

    else:
        break
