import os
os.system("clear")

soma = 0
contadorNumero = 0

while True:
    numero = float(input("Digite o número: "))

    if numero > 0:
        contadorNumero += 1
        soma += numero

    elif numero < 0:
        print(f"Não foi informado nenhum número positivo.")
        input("Pressione uma tecla para continuar...")
        os.system("clear")
        media = soma / contadorNumero    
        print(f"Média: {media}")
        break
