#Peça dois números e uma operação. Use try-except-else-finally para tratar erros como divisão por zero e operação inválida.
#Utilize a estrutura match case para decidir com os caracteres abaixo suas respectivas operações: adição, subtração, multiplicação, divisão.

try:
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    escolha = input("Digite uma operação: (+, -, *, /) => ")

    match escolha:
        case "+":
            resultado = a + b
       
        case "-":
            resultado = a - b
        
        case "*":
            resultado = a * b

        case "/":
            resultado = a / b
        
        case _:
            raise ValueError("Operação inválida!")


except ZeroDivisionError:
    print ("Erro: Divisão por zero!")
except ValueError as e:
    print(f"{e}")
else:
    print(f"Resultado: {resultado}")
finally:
	print("Cálculo encerrado!")

#Google Colab --> permite usar arquivos .csv e .xls sem precisar instalar as bibliotecas (feito para análise de dados).
#Olhar print no celular.