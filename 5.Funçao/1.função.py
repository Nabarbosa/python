import os

#Função sem retorno
def logoSenai():
    os.system("clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

#Solicitando dados para o usuario
logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))
logoSenai()
segundoNumero = int(input("Digite o sugundo número"))

soma = somar(primeiroNumero, segundoNumero)

print(f"Soma: {soma}")

"""
#Solicitando dados para o usuario
logoSenai()
nome = input("Digite o seu nome: ")

logoSenai()
idade = int(input("Digite sua idade: "))

logoSenai()
peso = float(input("Digite seu peso: "))

#Exibindo dados para o usuario
logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")
"""