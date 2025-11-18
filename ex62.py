# Você foi contratado para analisar uma planilha de músicas chamada ClassicDisco.csv, contendo informações sobre músicas clássicas de discoteca, com as seguintes colunas:
# Artista​ / Musica​ / Ano​ / Genero​. Seu objetivo é explorar os dados usando diferentes métodos da biblioteca Pandas.

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtro = df['Artist']
print(filtro)

