import numpy as np

ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

print('=======================================================================\n')

Sucesso = np.mean(ds[1:, 7] == 'Success') * 100

print('Porcentagem de missões que deram certo: ', Sucesso, '%\n')

print('=======================================================================\n')

gastos = ds[1:, 6].astype(float)

gastos = gastos[gastos > 0]

media = np.mean(gastos)

print('Custo médio das missoes: ', media,'\n')

print('=======================================================================\n')

missoes = np.char.strip(ds[1:, 2])

qtd_USA = missoes[np.char.endswith(missoes, 'USA')]

print('Quantidade de missões realizadas pelos EUA: ', qtd_USA.size, '\n')

print('=======================================================================\n')

spacex = ds[1:, 1] == 'SpaceX'

missoes_spacex = ds[1:, 4][spacex]

valores_spacex = ds[1:, 6].astype(float)[spacex]

maior_valor = valores_spacex.max()

mais_caras = ', '.join(missoes_spacex[valores_spacex == maior_valor])

print('As missões mais caras da SpaceX: ', mais_caras,', custando: ', maior_valor, ' milhoes\n')

print('=======================================================================\n')

empresa, quantidade = np.unique(ds[1:, 1], return_counts=True)

for emp, qtd in zip(empresa, quantidade):
    print('A empresa ', emp, 'realizou: ', qtd, ' missoes \n')