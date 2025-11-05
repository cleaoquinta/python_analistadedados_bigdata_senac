n1=float(input("Digite nota 1 "))
n2=float(input("Digite nota 2 "))
n3=float(input("Digite nota 3 "))
n4=float(input("Digite nota 4 "))
mean=(n1+n2+n3+n4)/4
print(f"A média é {mean}")
if  (mean >= 6):
    print("O aluno está APROVADO")
else:
    print("O aluno está em RECUPERAÇÃO")