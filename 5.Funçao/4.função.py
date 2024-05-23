import os
os.system("cls || clear")

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def multiplicacao(n1, n2):
    return n1 * n2

logoSenai()
numero = int(input("Digite um número: "))

logoSenai()
for i in range(1 , 11):
    multiplicar = multiplicacao(numero, i)
    print(f"{numero} x {i} = {multiplicar}")


