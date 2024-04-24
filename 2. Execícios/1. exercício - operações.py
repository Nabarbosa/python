import os

os.system("cls || clear")

print("=== Solicitando dados ===\n")
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = (primeiroNumero + segundoNumero)
subtracao = (primeiroNumero - segundoNumero)
multiplicacao = (primeiroNumero * segundoNumero)
divisao = (primeiroNumero / segundoNumero)

print("=== Exibindo resultados ===\n ")
print(f"Primeiro Número: {primeiroNumero}")
print(f"Segundo Número: {segundoNumero}")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")