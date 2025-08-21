#Exercicio 1

import numpy as np

arr = np.ones(8)

arr2 = np.random.randint(0, 10, 8)

print('NumPy Array 1: ', arr)

print('NumPy Array 2: ', arr2)

arr3 = arr + arr2

soma = arr3.sum()

print('Array resultante: ')

print('Soma dos elementos dos dois: ', soma)

if soma >= 40:
    mtz = arr3.reshape(4, 2)

if soma < 40:
    mtz = arr3.reshape(2, 4)

print('Resultado final: \n')

print(mtz, '\n')

print('====================================================================\n')

#Exercício 2

arr4 = np.arange(0, 52, 2)

arr5 = np.arange(100, 49, -2)

print('Array 1: ', arr4)

print('Array 2: ', arr5)

concatenado = np.concatenate((arr4,arr5))

print('Numpy Arrays concatenados: ', concatenado)

print('Numpy Arrays ordenados: ', np.sort(concatenado), '\n')

print('====================================================================\n')

#Exercicio 3

mtz2 = np.zeros((2, 2), dtype = int)

linha = np.random.randint(0, 2)

coluna = np.random.randint(0, 2)

mtz2[linha, coluna] = 1

cont = 0

tentativas = 3

achou = False

while cont < tentativas and not achou:
    print('Tentativa atual: ', (cont + 1), '\n')

    lin = int(input('Digite a posicao da linha 0 ou 1: '))

    col = int(input('Digite a posicao da coluna 0 ou 1: '))

    if mtz2[lin, col] == 1:
        print('Game Over! :( Try Again!\n')

        achou = True
    else:
        print('Aqui esta limpo! \n')
    
    cont += 1

if not achou:
    print('Congratulations! You beat the game! :) \n')

print('====================================================================\n')

#Exercicio 4

linhas = np.random.randint(2, 5)

colunas = np.random.randint(2, 5)

mtz3 = np.random.randint(0, 10, (linhas, colunas))

print('Matriz gerada:\n', mtz3, '\n')

print('Numero de linhas: ', linhas, '\n')

print('Numero de colunas: ', colunas, '\n')

vetor = mtz3.reshape(-1)

print('Vetor unitario: ', vetor, '\n')

total = linhas * colunas

if total % 2 == 0:
    print('O vetor e par \n')
else:
    print('O vetor e impar \n')

print('====================================================================\n')

#Exercicio 5

seed = np.random.seed(10)

mtz4 = np.random.randint(1, 51, (4, 4))

print('Matriz gerada: \n', mtz4)

mlinha = np.mean(mtz4, axis = 1)

mcoluna = np.mean(mtz4, axis = 0)

print('\n')

print('Media de cada linha: ', mlinha, '\n')

print('Media de cada coluna: ', mcoluna, '\n')

print('Maior valor da media de linhas: ', mlinha.max(), '\n')

print('Maior valor da media de colunas: ', mcoluna.max(), '\n')

numero, cont2 = np.unique(mtz4, return_counts = True)

print('Quantidade de vezes que os numeros aparecem: \n')

for n, c in zip(numero, cont2):
    print('O numero ', n, ' aparece ', c, ' vezes', '\n')

numero_repetido = numero[cont2 == 2]

print('Numeros que aparecem 2 vezes: ', numero_repetido)