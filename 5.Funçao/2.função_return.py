import os

# Sem retorno
def logoSenai():
    os.system("clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

# Com retorno
def somar(n1, n2):
    resultado = n1 + n2
    return resultado

def subtrair(n1, n2):
    resultado = n1 - n2
    return resultado

def divisar(n1, n2):
    resultado = n1 / n2
    return resultado

def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado

#Solicitando dados para o usuario
logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))
logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
subtracao = subtrair(primeiroNumero, segundoNumero)
divisao = divisar(primeiroNumero, segundoNumero)
multiplicacao = multiplicar(primeiroNumero, segundoNumero)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Divisão: {divisao:.2F}")
print(f"Multiplicação: {multiplicacao}")