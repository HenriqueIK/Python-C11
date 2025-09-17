import pandas as pd

import numpy as np

df = pd.read_csv('paises.csv', delimiter=';')

paisesOceania = df.loc[df['Region'].str.contains('OCEANIA')]

print('========================================================================\n')

print('Paises da Oceania:\n' , paisesOceania['Country'])

print('========================================================================\n')

print('Numero de paises na Oceania:',np.size(paisesOceania['Country']),'\n')

print('========================================================================\n')

maiorPop = df.loc[df['Population'] == df['Population'].max()]

print('Pais com a maior populacao:\n', maiorPop[['Country', 'Population']], '\n')

print('Na região:\n', maiorPop['Region'],'\n')

print('========================================================================\n')

grupoReg = groupby = df.groupby('Region')

media = grupoReg['Literacy (%)'].mean()

print('Média de alfabetização por região (%):\n', media, '\n')

print('========================================================================\n')

noCoast = df.loc[df['Coastline (coast/area ratio)'] == 0]

noCoast.to_csv('noCoast.csv', sep=';')

print('=========================================================================\n')

def mortalidade(Deathrate):
    if Deathrate < 9:
        return 'Balanced'
    else:
        return 'Urgent'

df['Humanitarian Help'] = df['Deathrate'].apply(mortalidade)

print(df[['Country', 'Deathrate', 'Humanitarian Help']])

print('=========================================================================\n')