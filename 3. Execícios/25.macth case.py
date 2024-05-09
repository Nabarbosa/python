import os
import sys

os.system("cls||clear")

maiorIdade = 0
menorIdade = sys.maxsize
mulheres5k = 0
somaSalarios = 0
quantidadeSalarios = 0
mediaSalarios = 0

while True:
    print("=== Menu ===\n")
    print(" Código |  Descrição")
    print("    1   | Adicionar pessoa")
    print("    2   | Exibir Resultados e sair\n")
    opcao = int(input("Escolha uma opção: "))

    match(opcao):
        case 1:
            print("=== Solicitando dados ===")
            idade = int(input("Digite a idade: "))

            while idade < 0 or idade > 120:
                idade = int(input("=== Idade inválida! \n Digite a idade novamente: "))

            sexo = input("Digite o sexo (M ou F): ")
            sexo = sexo.upper()

            while sexo != "F" and sexo != "M":
                sexo = input("=== Sexo inválido! \n Digite o sexo (M ou F) novamente: ")
                sexo = sexo.upper()

            salario = float(input("Digite o salário: "))
            while salario < 0:
                salario = float(input("=== Salário inválido! \n Digite o salário novamente: "))
           
            somaSalarios += salario
            quantidadeSalarios += 1

            maiorIdade = max(idade, maiorIdade)
            menorIdade = min(idade, menorIdade)

            if sexo == "F" and salario >= 5000:
                mulheres5k += 1

            if quantidadeSalarios != 0:
                mediaSalarios = somaSalarios / quantidadeSalarios
       
        case 2:
            print("=== Mostrando resultados ===")
            print(f"Média de salários do grupo: R$ {mediaSalarios:.2f}")
            print(f"Maior idade do grupo: {maiorIdade}")
            print(f"Menor idade do grupo: {menorIdade}")
            print(f"Mulheres com salário a partir de 5 mil: {mulheres5k}")
            break
        case _:
            print("Opção inválida. \nTente novamente.")