import os

os.system("cls||clear")

contadorNotas = 0
soma = 0

while True: 
    nota = float(input(f"Digite uma nota: "))
    resposta = input(f"Deseja inserir mais uma nota? ")

    #Converter o texto digitado em maiúsculo.
    reposta = resposta.upper()

    if resposta != "n":
        contadorNotas += 1
        soma += nota
    else:
        break    

    """
    if resposta == "N"
        break
    else:
        soma += nota
        contadorNotas += 1
    """

media = soma / contadorNotas

print(f"\n=== Exibindo resultados ===")
print(f"\nMédia: {media}")

