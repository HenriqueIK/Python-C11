#Exercicio 4

nome = []

peso = []

for i in range(0, 3):
    nomePessoa= str(input("Digite o nome da pessoa:"))

    pesoPessoa = float(input("Digite o peso da pessoa:"))

    nome.append(nomePessoa)

    peso.append(pesoPessoa)

print("A pessoa mais pesada:", nome[peso.index(max(peso))])

print("A pessoa mais leve:", nome[peso.index(min(peso))])

print('=======================================================================')

#Exercicio 5

lista = []

num = int(input('Digite a quantidade de pessoas: '))

var1 = 0

var2 = 0

for i in range(num):
    nome = str(input('Digite o nome da pessoa: '))

    idade = int(input('Digite a idade da pessoa: '))

    var1 += idade
    
    s = str(input('Digite o sexo da pessoa (M ou F): '))

    while(s != 'M' and s != 'F'):
        s = input('Entre com um sexo valido: ')
    
    if(s == 'F' and idade < 20):
        var2 += 1
    
    pessoas = {'Nome': nome, 'Idade': idade, 'Sexo': s}

    lista.append(pessoas)

print(pessoas)

media = var1 / num

print('Media da idade das pessoas:', media)

print('Numero de mulheres com menos de 20 anos:', var2)