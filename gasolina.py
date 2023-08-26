import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv')

grafico = sns.lineplot(data=gasolina_df, x='dia',y='venda')
grafico.set(title='Preço diário da gasolina')
grafico.set_xlabel('Dia')
grafico.set_ylabel('Venda')

plt.savefig('gasolina.png')