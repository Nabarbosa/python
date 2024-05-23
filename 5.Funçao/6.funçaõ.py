"""
Fazer um programa que solicita o preço de um produto
e inflaciona esse preço em 10% se ele for menor que 100 e 20%
se ele for maior ou igual a 100.
"""
def logoSenai():
    os.system("cls || clear")
    print("===== ============ =====")
    print("===== SENAI | FIEB =====")
    print("===== ============ =====")

def inflacionar(preco):
    novoPreco = 0
    if preco < 100:
        novoPreco = preco * 1.0
    else:
        novoPreco = preco * 2.0
    return novoPreco

logoSenai()
preco = float(input("Imforme o preço: "))

precoAtual = inflacionar(preco)

logoSenai()
print(f"Preço novo: {precoAtual}")