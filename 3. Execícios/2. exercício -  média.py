import os

os.system("cls || clear")

print("\n === Solicitando dados === \n")

# Não precisa colocar o "str", o "input" já leva como texto.

nome = (input("\nDigite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))

soma = (primeiraNota + segundaNota) / 2

os.system("cls || clear")

print("\n === Exibindo resultados ===\n")
print(f"Nome do aluno: {nome}")
print(f"Idade do aluno: {idade}")
print(f"Primeira nota do aluno: {primeiraNota}")
print(f"Segunda nota do aluno: {segundaNota}")
print(f"Média do aluno: {soma}")