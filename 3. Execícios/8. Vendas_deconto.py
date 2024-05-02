import os

os.system("cls || clear")

print("==== Opção: ")
print("==== Morangos")
print("==== Maçãs\n")

nome = (input("Digite o nome do produto: "))
quantidade = int(input("Digite a quantidade em Kg dos produtos: "))

if nome == "maçãs" and quantidade <= 5:
    preco = 2.50
else:
    preco = 2.20

if nome == "morangos" and quantidade <= 5:
    preco = 1.80
else:
    preco = 1.50

valor = quantidade * preco    

print(f"Nome do produto: {nome}")
print(f"Preço do produto escolhido: {preco}")
print(f"Quantidade do produto: {quantidade}")
print(f"Total a pagar: {valor}")

if quantidade > 8 and valor > 25:
    totalDesconto = valor - (valor * 0.10) 
    print(f"Você possui desconto!")
    print(f"Total a pagar com o desconto: {totalDesconto}")
else:
    print(f"Não possui desconto!")