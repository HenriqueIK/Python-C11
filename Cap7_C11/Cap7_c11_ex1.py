import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df_co2 = pd.read_csv('co2_emissions.csv', delimiter = ',', index_col = 'Year', parse_dates = True)

df_co2['CO2_Emissions'] = df_co2['CO2_Emissions'].astype(float)

df_co2['CO2_Emissions'].plot(figsize = (8,6),
title = 'Índice de emissões de CO2',
xlabel = "Ano", 
ylabel = "Emissões de CO2",
x_compat = True
)
plt.show()

decomposition = seasonal_decompose(df_co2['CO2_Emissions'], model = 'additive')

decomposition.plot()
plt.tight_layout()
plt.show()

# a) A Série possui Tendência?
# R: Sim, Decrescente

# b) A série possui sazionalidade?
# R: Não

# c) A série possui um ciclo?
# R: Sim, a cada 8 anos os níveis de emissão de C02 voltam a subir, mas depois caem