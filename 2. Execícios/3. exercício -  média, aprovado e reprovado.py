import os

os.system("cls || clear")

print("\n === Solicitando dados === \n")
nome = (input("\nDigite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = int(input("Digite a primeira nota: "))
segundaNota = int(input("Digite a segunda nota: "))
terceiraNota = int(input("Digite a terceira nota: "))

soma = (primeiraNota + segundaNota + terceiraNota) / 3

os.system("cls || clear")

print("\n === Exibindo resultados ===\n")
print(f"Nome do aluno: {nome}")
print(f"Idade do aluno: {idade}")
print(f"Média do aluno: {soma}\n")

if soma < 7:
    print("=== Reprovado ===")
else:
    print("=== Aprovado ===")    