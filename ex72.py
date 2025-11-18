import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

# Filtrar músicas lançadas depois de 1980 e mostrar apenas colunas "Year" e "Track"
print(df[df['Year'] > 1980][['Year', 'Track']])
