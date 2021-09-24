"""
iteráveis:
 - String
    nome = 'Geek University'

 - Lista
    lista = [1, 3, 5, 7, 9]

 - Range
    numeros = range [1,10]
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
"""
range = range(1, 10)

for letra in nome:
    print(letra)

for numero in lista:
    print (numero)

for numero in range:
    print (numero)


Enumerate:
retorna indice,letra

for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print (letra)

for valor in enumerate(nome):
    print (valor[0],valor[1])
    print (valor)

qtd = int(input('Quantas vezess esse loop deve rodar? '))
soma = 0

for n in range(1,qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

for letra in nome:
    print(letra, end='')
"""

for _ in range(3):
    for num in range(1,11):
        print('\U0001F60D' * num)
