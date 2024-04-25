import os

os.system("cls || clear")

print("Morangos")
print("Maçãs")

nome = (input("Digite o nome do produto: "))
quantidade = int(input("Digite a quantidade em Kg dos produtos: "))

if nome == "maçãs" and quantidade <= 5:
    preco = 2.50
else:
    preco = 2.20
if nome == "morangos" and quantidade <= 5:
    preço = 1.80
else:
    preco = 1.
    
valor = quantidade * preco    

if quantidade > 8 and valor > 25.00:
    desconto = 0.1        

print(f"Nome do produto: {nome}")
print(f"Quantidade do produto: {quantidade}")
print(f"Preço do produto: {preco}")
print(f"Total a pagar: {valor}")
