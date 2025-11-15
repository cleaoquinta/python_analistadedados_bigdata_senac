#Ler duas notas, calcule a média e trate erros de entrada (valor inválido ou divisão incorreta).

def media (a, b):
    try:
        #TESTE
        resultado = (a + b)/2
    except ZeroDivisionError:
        # erro
        print("Erro: Divisao por zero nao é permitida!")
    else:
        # EXECUTAR QUANDO NÃO HOUVER ERRO
        print(f"Resultado da média do aluno: {resultado}")
    finally:
        # EXECUTAR SEMPRE
        print(f"Nota final do bimestre: {round (resultado, 1)}")

# Programação principal
try:
    num1 = float(input("Digite a primeira nota => "))
    num2 = float(input("Digite a segunda nota => "))
    media (num1, num2)
except ValueError:
    print("Voce deve digitar apenas números!") 
    