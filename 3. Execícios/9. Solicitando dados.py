import os
os.system("cls||clear")

nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo 'F' ou 'M': ")
estadoCivil = input("Imforme o seu estado civil: ")  

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == "f" and estadoCivil == "casada":
    tempoCasada = int(input("Informe quantos anos de casamento: "))

print("\n=== Exibindo resultados ===")
print(f"Nome: {nome}")    
print(f"Sexo: {sexo}")    
print(f"Estado Civil: {estadoCivil}")    
    
if sexo == "f" and estadoCivil == "casada":
    print(f"Tempo de casamento: {tempoCasada}")