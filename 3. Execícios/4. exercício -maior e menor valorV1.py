import os

os.system("cls || clear")

primeiroValor = int(input("Digite o primeiro número: "))
segundoValor = int(input("Digite o segundo número: "))

soma = primeiroValor + segundoValor
produto = primeiroValor * segundoValor
media = soma / 2

if primeiroValor > segundoValor:
    maiorValor = primeiroValor
else:
    maiorValor = segundoValor

if primeiroValor < segundoValor:
    menorValor = primeiroValor
else:
    menorValor = segundoValor          

os.system("cls || clear")

print("=== Exibindo resultados ===")
print(f"Primeiro valor: {primeiroValor}")
print(f"Segundo valor: {segundoValor}")
print(f"Soma: {soma}")    
print(f"Produto: {produto}")    
print(f"Média: {media}")    
print(f"Maior valor: {maiorValor}")    
print(f"Menor valor: {menorValor}")    