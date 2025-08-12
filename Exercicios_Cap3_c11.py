#Exercicio 1

times = ['Arsenal', 'Bragantino', 'Gremio', 'Barcelona', 'Flamengo']

print('Primeiros colocados:')

for i in range (0, 3):
    print(times[i])

print('Ultimos colocados:')

for j in range (3, 5):
    print(times[j])

print('O Barcelona se encontra em:', times.index('Barcelona'))

print('Times na ordem alfabetica: ')

times.sort()

print(times)

print('=======================================================================')

#Exercicio 2

loja1 = {'Samsung', 'Motorola', 'Xiaomi','LG'}

loja2 = {'Iphone', 'Xiaomi', 'Motorola', 'Nokia'}

print('Opcoes de compra na primeira loja:', loja1)

print('Opcoes de compra na segunda loja:', loja2)

print('Todos os Smartphones que voce encontra visitando as duas lojas:', loja1 | loja2)

print('Smartphones que voce encontra em ambas as lojas:', loja1 & loja2)

print('=======================================================================')

#Exercicio 3

nomeAluno = str(input('Digite o nome do aluno: '))

mediaAluno = int(input('Digite a media do aluno: '))

if mediaAluno >= 50:
    print('Aluno', nomeAluno, 'Aprovado')
elif mediaAluno < 50:
    print('Aluno', nomeAluno, 'Reprovado')

aluno = {'nome': nomeAluno, 'media': mediaAluno}

print(aluno)