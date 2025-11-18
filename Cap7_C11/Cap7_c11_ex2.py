import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df_air = pd.read_csv('airtravel.csv', delimiter = ',', index_col = 'Date', parse_dates = True)

df_air['Passengers'] = df_air['Passengers'].astype(float)

df_air['Passengers'].plot(figsize = (8,6),
title = 'Índice de passageiros de 1958 a 1960',
xlabel = "Data", 
ylabel = "Quantidade de passageiros",
x_compat = True
)
plt.show()

decomposition = seasonal_decompose(df_air['Passengers'], model = 'additive')

decomposition.plot()
plt.tight_layout()
plt.show()

# a) A Série possui Tendência?
# R: Sim, Crescente

# b) A série possui sazionalidade?
# R: Sim, no período das férias de Junho, Julho e Agosto(Meses 6,7 e 8) o número de viagens aéreas aumentam

# c) A série possui um ciclo?
# R: Sim, uma vez a cada ano entre Junho e Agosto, as viagens e número de passageiros aumentam