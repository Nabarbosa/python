import os 
import time

os.system("cls||clear")

somasalario = 0
quantidadeMulheres = 0
maiorIdade = 0
menorIdade = 999
quantidadeSalario = 0

while True:
    print("=== Menu ===\n")
    print(" Código |  Descrição")
    print("    1   | Adicionar pessoa")
    print("    2   | Exibir Resultados e sair\n")

    opcao = int(input("Escolha uma opção: "))
    os.system("clear")
    
    if opcao == 1:
        idade = int(input("Digite sua idade: "))
        sexo = input("Digite o seu sexo (F ou M): ")
        salario = float(input("Informe os seu salário: "))
        quantidadeSalario += 1
        somasalario += salario
        mediaSalario = somasalario / quantidadeSalario
        os.system("clear")

        sexo = sexo.upper()    

        if sexo == "F" and salario >= 5000:
            quantidadeMulheres += 1
    
    maiorIdade = max(idade,maiorIdade)
    menorIdade = min(idade,menorIdade)

    if opcao == 2:
        print("\n  ==== Exibindo Resultados ==== \n")
        print(f" Média salário: R$ {mediaSalario:.2F}")
        print(f" Maior idade do grupo: {maiorIdade}")
        print(f" Menor idade do grupo: {menorIdade}")
        print(f" Quatidade de mulheres com o salário a partir de R$ 5000,00: {quantidadeMulheres}")
        break

    elif opcao != 1 and opcao != 2:
        print("Foi informada uma opção que não existe...")
        time.sleep(2)
        os.system("clear")

