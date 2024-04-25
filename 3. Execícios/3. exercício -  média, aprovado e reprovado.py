import os

os.system("cls || clear")

print("\n === Solicitando dados === \n")
nome = (input("\nDigite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = int(input("Digite a primeira nota: "))
segundaNota = int(input("Digite a segunda nota: "))
terceiraNota = int(input("Digite a terceira nota: "))

media = (primeiraNota + segundaNota + terceiraNota) / 3

#if media >= 7:
#   resultado = "Aprovado"
#else:
#    resultado = "Reprovado"    

os.system("cls || clear")

print("\n === Exibindo resultados ===\n")
print(f"Nome do aluno: {nome}")
print(f"Idade do aluno: {idade}")
print(f"Média do aluno: {media}")
#print(f"Resultado: {Resultado}\n")

if media >= 7:
    print("=== Aprovado ===")    
else:
    print("=== Reprovado ===")