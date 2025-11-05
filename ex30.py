#tentar fazer juntando produtos diferentes
produto1 = input("Digite o produto que deseja comprar -> ").upper ()
print (produto)
if (produto1 == "MOUSE"):
    preco1 = 10.00 
elif (produto1 == "TECLADO"):
    preco1 = 20.00
elif (produto1 == "MEMORIA"):
    preco1 = 100.00
else:
    preco1 = 0
    print ("Não vendemos este produto.")
    outro = input("Deseja comprar mais um produto diferente? S ou N. -> ").upper ()
    if (outro == S):
        if (produto2 == "MOUSE"):
            preco2 = 10.00 
        elif (produto2 == "TECLADO"):
            preco2 = 20.00
        elif (produto2 == "MEMORIA"):
            preco2 = 100.00
        else:
            preco2 = 0.00
        print ("Não vendemos este produto.")
    if (preco1 == 0 or ):
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
    elif (outro == N):
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

else:
    preco = 0.00
    print ("Não vendemos este produto.")
input("Deseja comprar mais um produto diferente? -> ").upper ()
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