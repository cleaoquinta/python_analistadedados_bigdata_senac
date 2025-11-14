#Crie uma função que receba dois números e retorne o maior deles.

def maior(a, b):
    if a >= b:
        return a
    else:
        return b

#Interação com o usuário:
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

#Chamada da função e exibição do resultado:
maior_num = maior(n1, n2)
print(f"O maior número entre {n1} e {n2} é {maior_num}!")

