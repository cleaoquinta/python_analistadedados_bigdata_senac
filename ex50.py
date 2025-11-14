#Crie uma função que receba um nome como argumento (string) e retorne uma mensagem de saudação completa.

def saudar(nome):
    return f"Olá, {nome}! Seja bem-vindo(a) ao mundo Python!"

#Interação com o usuário:
nome_usuario = input("Digite seu nome ")

#Chamada da função e exibição do resultado
mensagem = saudar(nome_usuario)
print(mensagem)ex3