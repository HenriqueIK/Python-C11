import numpy as np

ds = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

#Questao 1

pais = ds[1:, 0]
reg = ds[1:, 1] #regiao
pop = ds[1:, 2] #populacao
area = ds[1:, 3]

print(pais, '\n')
print(reg, '\n')
print(pop, '\n')
print(area, '\n')

#Questao 2

ru = np.unique(reg) #regiao unica

print('Regiao unica de cada pais: ', ru, '\n')

#Questao 3

alf = ds[1:, 9].astype(float) #alfabetizacao(%)

media = np.mean(alf)

print('Media de alfabetizacao: ', media, '%\n')

#Questao 4

num = np.char.find(reg, 'NORTHERN AMERICA') >= 0

print('Quantidade de paises na America do Norte: ', num.sum(), '\n')

#Questao 5

num2 = ds[1:, 8].astype(float)

reg == 'LATIN AMER. & CARIB'

gdp = num2[reg == 'LATIN AMER. & CARIB']

print('O maior GPD da Ameria Latina e Caribe: ', gdp.max())