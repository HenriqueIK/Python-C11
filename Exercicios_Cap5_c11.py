import pandas as pd

import numpy as np

# Exercicios parte 1

print('=======================================================================================\n')

linguagens = ['Java', 'C', 'Python']

porcentagem = [16.25, 16.04, 9.85]

dic = {'Java': 16.25, 'C': 16.04, 'Python': 9.85}

seriesAno1 = pd.Series(data=linguagens, index=porcentagem)

seriesAno1 = pd.Series(dic)

porcentagem2 = [11.68, 16.21, 12.12]

dic2 = {'Java': 11.68, 'C': 16.21, 'Python': 12.12}

seriesAno2 = pd.Series(index=linguagens, data=porcentagem2)

seriesAno2 = pd.Series(dic2)

print('Series: \n')

print(seriesAno1, '\n')

print(seriesAno2, '\n')

print('=======================================================================================\n')

print('No ano 1, as linguagens C, Python e Java correspondem à', seriesAno1.sum(), '%\n')

print('No ano 2, as linguagens C, Python e Java correspondem à', seriesAno2.sum(), '%\n')

print('=======================================================================================\n')

subtracao = (seriesAno2 - seriesAno1)

print('Crescimento/Declínio de cada linguagem(%):\n', subtracao, '\n')

print('=======================================================================================\n')

print('As linguagens que cresceram foram(%):\n', (subtracao[subtracao > 0]), '\n')

print('=======================================================================================\n')

seriesAno3 = seriesAno2 + subtracao
seriesAno4 = seriesAno3 + subtracao

print('Linguagens no ano 3:\n', seriesAno3, '\n')

print('Linguagens no ano 4:\n', seriesAno4, '\n')

linguagem_final = seriesAno4.nlargest(1)

print('Linguagem mais popular no ano 4:', linguagem_final, '\n')

print('=======================================================================================\n')

# Exercicios parte 2

df = pd.DataFrame(index = ['A', 'B', 'C', 'D', 'E'],
                  columns = ['W', 'X', 'Y', 'Z'],
                  data = np.random.randint(1, 50, [5, 4]))

print(df, '\n')

media = df.loc[df['X'] < 30, 'X'].mean()

print('A media de elementos na coluna X com valores menores que 30:', media, '\n')

print('=======================================================================================\n')

media2 = df.loc['D'].mean()

print('Media de valores da linha D:', media2, '\n')

soma = df.iloc[4].sum()

print('Soma dos valores da linha E:', soma, '\n')

print('=======================================================================================\n')

slicing = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print('Slicing:\n', slicing, '\n')

soma_linha = slicing.sum(axis = 1)

soma_coluna = slicing.sum(axis = 0)

print('Soma dos elementos das linhas A, C e E:\n', soma_linha, '\n')

print('Soma dos elementos das colunas X e Y:\n', soma_coluna, '\n')

print('=======================================================================================\n')