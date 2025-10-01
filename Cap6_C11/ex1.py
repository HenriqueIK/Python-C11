import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

df_paises = pd.read_csv('paises.csv', delimiter = ';')

df_paises['Region'] = df_paises['Region'].str.strip()
df_paises['Country'] = df_paises['Country'].str.strip()

df_paises['Deathrate'] = pd.to_numeric(df_paises['Deathrate'], errors='coerce')
df_paises['Birthrate'] = pd.to_numeric(df_paises['Birthrate'], errors='coerce')

am_norte = df_paises[df_paises['Region'] == 'NORTHERN AMERICA']

am_norte = am_norte.dropna(subset=['Deathrate', 'Birthrate'])

am_norte = am_norte.sort_values('Country')

paises = am_norte['Country']

plt.plot(paises, am_norte['Deathrate'], '*:r', label='Taxa de Mortalidade (Deathrate)', marker='o')

plt.plot(paises, am_norte['Birthrate'], 's--g' , label='Taxa de Natalidade (Birthrate)', marker='o')

plt.title('Taxas de Mortalidade e Natalidade (America do Norte)')
plt.xlabel('Paises da America do Norte')
plt.ylabel('Taxas')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()