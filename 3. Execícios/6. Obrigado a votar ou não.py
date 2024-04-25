import os

os.system("cls || clear")

print("=== Solicitand dados === ")
idade = int(input("Digite sua idade: "))

if idade <= 18 and idade >= 65:
    print("Obrigatório votar!")    
else:
    print("NÃO é origatório votar!")