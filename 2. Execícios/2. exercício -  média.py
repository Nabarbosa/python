import os

os.system("cls || clear")

print("\n === Solicitando dados === \n")
# Não precisa colocar o "str" o "input" já leva como texto.
nome = str(input("\nDigite seu nome: "))
idade = int(input("\nDigite sua idade: "))
primeiraNota = int(input("\nDigite a primeira nota: "))
segundaNota = int(input("\nDigite a segunda nota: "))

soma = (primeiraNota + segundaNota) / 2

print("\n === Exibindo resultados ===\n")
print(f"Nome do aluno: {nome}\n")
print(f"Idade do aluno: {idade}\n")
print(f"Primeira nota do aluno: {primeiraNota}\n")
print(f"Segunda nota do aluno: {segundaNota}\n")
print(f"Média do aluno: {soma}\n")