import os

os.system("cls || clear")

login = "Marta"
senha = "123"

login = (input("Digite o seu login: "))
senha = (input("Digite a sua senha: "))

if login == "Marta" and senha == "123":
    print("Bem-vindo!")
else:
    print("Login ou senha inválidos!")    