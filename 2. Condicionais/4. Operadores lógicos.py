import os

os.system("cls || clear")

sexo = input("Informe o sexo [M ou F]: ")
idade = int(input("Digite sua idade: "))

if sexo == "M" and idade == 18:
    print("Alistamento militar obrigatório.")
else:
    print("Alistamento militar NÃO obrigatório.")

print("=== FIM ===")        