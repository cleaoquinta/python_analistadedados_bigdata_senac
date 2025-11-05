#Estudo de caso: Você foi contrato pelo exercíto brasileiro para desenvolver um sistema de alistamento militar, onde se le o ano de nascimento do candidato e o genero, o sistema irá calcular a idade, se a idade for maior igual a 18 e o sexo masculino ele estará apto a se alistar, senão não apto
anonasc = int(input("Digite o ano de nascimento -> "))
genero = input("Digite sexo M ou F -> ").upper()
#print(anonasc)
#print(genero)
idade = 2025 - anonasc
if (idade >=18 and genero == "M"):
    print("Apto a se alistar")
else:
    print("Não apto")