#Desenvolver um código python que leia um cargo de funcionário e, de acordo com o cargo, mostre o salário. Vide tabela abaixo: Caixa - 1.500; Vendedor - 2.400; Gerente - 4.000
#De acordo com os salários acima, calcule: a) INSS = 12% sobre o salário; b) IRRF se salário for maior que 2000 o IRRF será de 14% sobre o salário, senâo será de 8%; c) salário final = salário - IRRF - INSS.
cargo = input("Digite seu cargo -> ").upper ()
print (cargo)
if (cargo == "CAIXA"):
    salario = 1500.00 
elif (cargo == "VENDEDOR"):
        salario = 2400.00
elif (cargo == "GERENTE"):
        salario = 4000.00
else:
    salario = 0.00
    print ("Esse cargo não existe.")
inss = (salario)*(12/100)
if (salario > 2000):
    irrf= (salario)*(14/100)
else:
    irrf = (salario)*(8/100)
recebido = (salario) - (irrf) - (inss)
print (f"Seu salário líquido é R$ {recebido}")
print (f"Seus impostos pagos foram: R$ {inss} de INSS e R$ {irrf} de IRRF")
