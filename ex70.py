#O que é enumerate()​? O comando enumerate() é uma função embutida do Python que serve para numerar automaticamente os itens de uma sequência (lista, tupla, string, colunas de um DataFrame etc.).​
#Em vez de só percorrer os itens, ele te dá também o índice (posição) de cada item.​

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

#Exibindo as colunas enumeradas:
for i, coluna in enumerate(df.columns, start=1):
    print(f"{i}ª coluna: {coluna}")
