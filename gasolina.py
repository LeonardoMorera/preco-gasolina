import pandas as pd
import seaborn as sns
import os
from getpass import getpass

gasolina_df = pd.read_csv('gasolina.csv')
gasolina_df.head()

grafico = sns.lineplot(data=gasolina_df, x='dia',y='venda')
grafico.set(title='Preço diário da gasolina')
grafico.set_xlabel('Dia')
grafico.set_ylabel('Venda')