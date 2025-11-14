#Crie uma função que receba o lado de um quadrado e retorne o valor da sua área ($A = lado^2$).

def quadrado(lado):
    return lado ** 2
#Usando o operador de exponenciação (**)

#Interação com o usuário:
medida_lado = float(input("Digite a medida do lado do quadrado: "))

#Chamada da função e exibição do resultado:
area = quadrado(medida_lado)
print(f"A área do quadrado é: {area}")