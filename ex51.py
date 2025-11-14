def par(numero):
    return numero % 2 == 0 # condição de true or false (variável boleana)
#O operador % (módulo) retrna o resto da divisão. Se resto da divisão de 2 for 0, é par.

#Interação com o usuário:
num = int(input("Digite um número inteiro: "))

#Chamada da função e exibição e exibição do resultado.
resultado = par(num) # gera uma variavel boleana

if resultado:
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é impar!")