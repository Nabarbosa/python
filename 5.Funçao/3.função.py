import os
os.system("cls || clear")

def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def calcular_media(n1, n2):
    return  (n1 + n2) / 2

logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))
logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

media = calcular_media(primeiroNumero, segundoNumero)

logoSenai()
print(f"Média: {media}")
    
    