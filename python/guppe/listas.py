"""
lista1 = [1, 99, 23, 2, 32, 1, 12, 12, 21, 12]

lista8 = [1, 99, 23, 2, 32, 1, 12, 12, 21, 12]

lista2 = ['c', 'd', ' ', 's', 'd', 'm', 'o']

lista3 = []

lista4 = [list(range(11))]

lista5 = list('Geek University')

print('inicio')

num = 'd'
if num in lista5:
    print("encontrei")
else:
    print("nao encontrei")

print(lista1)
lista1.sort()
print('ordenacao',lista1)
print('contar',lista1.count(1))
print(lista5.count("e"))
lista1.append(2)
lista1.append(3)
lista1.append(4)
lista1.append([2,3,4])
lista1.extend([3,6,82])
lista1.insert(3,"novo valor")
print('inserindo com append, ou extend, com insert na posicao desejada',lista1)

if [2,3,4] in lista1:
    print("Encontrei a lista")
else:
    print("Nao encontrei a lista")

lista6 = lista1 + lista5
print('juncao de listas',lista6)
lista1 = lista1 + lista5
lista1.reverse()
print('impressao reversa',lista1)
print(lista2)
print(lista2[::-1])
lista7 = lista2.copy()
print('tamanho da lista',len(lista7))
lista7.pop()
print('remove ultimo elemento',lista7)

print('limpeza da lista',lista5)
lista5.clear()
print(lista5)

nova = [1,2,3]
print('aumentadao tamanho da lista',nova)
nova = nova * 3
print(nova)

curso = 'Programacao em Python Essencial'
print(curso)
curso = curso.split()
print('separacao em lista a partir do espaco',curso)

lista8 = 'Programacao,em,python,essencial'
lista8 = lista8.split(',')
curso = ' '.join(lista8)
print(curso)
curso2 = ' @ '.join(lista8)
print(curso2)

soma = 5
for elemento in lista8:
    print(elemento)
    soma = soma + elemento
print(soma)

carrinho = []
produto = ''
while produto != 'sair':
    print("Adicionae um produto na lista ou digite 'sair', para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)


cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[-1])
print(cores[-2])
print(cores[-3])


cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1


cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores)

for indice, cor in enumerate(cores):
    print(indice, cor)

numeros = [5, 6, 7, 8, 9, 5, 10]

print(numeros.index(6))

print(numeros.index(9))

print(numeros.index(5, 1))

print(numeros.index(9, 2, 6))
"""
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

nova.append(4)

print(lista)
print(nova)

print(len(nova))
