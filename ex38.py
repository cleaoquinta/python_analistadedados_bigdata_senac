#Desenvolva um código python que leia 5 números e diga se cada número ao momento que for lido é par ou impar

for i in range(0,5):
    x=int(input("Digite um valor "))
    r = x % 2
    if r == 0:
        print(f"{x} é par!")
    else:
        print(f"{x} é impar!")