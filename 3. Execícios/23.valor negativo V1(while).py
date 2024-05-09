import os
import time
os.system("clear")

soma = 0
contadorNumero = 0

print("=== Solicitando Dados ===")
print(" \n=== Atenção ===\n \n Quando for informado um número negativo. \n Irá ser mostrado a média dos números digitados.")

while True:
    numero = float(input("\nDigite o número: "))
    os.system("clear")

    if numero >= 0:
        resposta = input("Deseja digitar mais um número? ")

        if resposta == "sim":
            contadorNumero += 1
            soma += numero

        elif resposta == "não":
            time.sleep(1)
            os.system("clear")
            print("informe um número negativo.")

        else:
            print("Foi informado uma resposta não registrada...")
            input("Pressione uma tecla para continuar...")
            os.system("clear")

    if numero < 0:
        os.system("clear")
        media = soma / contadorNumero    
        print(f"\n ===== Exinbindo Resultado ===== \n")
        print(f"Média dos números informados: {media}\n")
        break