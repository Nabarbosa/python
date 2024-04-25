import os

os.system("cls || clear")

nome = (input("Digite o nome do produto: "))
precoUnitario = float(input("Digite o preço unitário do produto: "))
quantidadeAdquirida = int(input("Digite a quantidade dos itens adiquiridos: "))

if quantidadeAdquirida <= 5:
    desconto = 0.02
elif quantidadeAdquirida <=10:
    desconto = 0.03
else:
    desconto = 0.05

"""
if quantidadeAdquirida <= 5:
    desconto = 0.02
if quantidadeAdquirida > 5 or quantidadeAdquirida <= 10:
    desconto = 0.03
if quantidadeAdquirida > 10:
    desconto = 0.05
"""

totalPagar = precoUnitario - (precoUnitario * desconto)

os.system("cls || clear")

print("=== Exibindo resultados ===")
print(f"Nome produto: {nome}")
print(f"Preço do produto: {precoUnitario}")
print(f"Quantidade do produto: {quantidadeAdquirida}")
print(f"Total a pagar: {totalPagar}")