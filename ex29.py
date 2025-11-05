#Uma loja de produtos tecnológicos te contratou para desenvolver um código da seguinte forma: (1) Leia um produto e de acordo com o produto verifique o preço.
#Tabela de preços: Mouse - 10; Teclado - 20; Memória - 100.
#Leia ainda a quantidade de produtos comprados. Calcule : a) valor total; b) imposto cobrado: se a quantidade for maior que 10 calcule 5% de imposto, senão calcule 10%; c) valor final.

produto = input("Digite o produto que deseja comprar -> ").upper ()
print (produto)
if (produto == "MOUSE"):
    preco = 10.00 
elif (produto == "TECLADO"):
       preco = 20.00
elif (produto == "MEMORIA"):
        preco = 100.00
else:
    preco = 0.00
    print ("Não vendemos este produto.")
if (preco == 0):
    print("Tente novamente!")
else:
    qtd = int(input("Digite a quantidade de produtos -> "))
    inicial = (preco)*(qtd)
    if (qtd>10):
        imp = (inicial)*(0.05)
    else:
        imp = (inicial)*(0.10)
    final = (inicial) + (imp)
    print (f"O valor a ser pago é R$ {final}")
    print (f"valor pago e impostos foi de R$ {imp}")

    #tentar fazer juntando produtos diferentes