"""
Funcoes com retorno

ret_pop = numeros = [1, 2, 3]

numeros.pop()

print(f'Retorno de pop:{ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Em Python, quando uma funcao nao retorna nenhum valor, o retorno e None

OBS: Funcoes Python que retornam valores, devem retornar estes valores com a plavra reservada return

OBS: Nao precisamos necessariamente criar uma variavel para receber o retorno de uma funcao.
Podemos passar a execucao da funcao para outras funcoes.


def quadrado_de_7():
    return 7 * 7

print(f'Retorno {quadrado_de_7() + 1}')

# Refatorando a primeira funcao

def diz_oi():
    return 'Oi!'

print(diz_oi())

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da funcao
2 - Podemos ter, em uma funcao, diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores

# Exemplo 1


def diz_oi():
    print('Estou sendo executado antes o retorno')
    return 'Oi!'
    print('apos o return nada é executado')


print(diz_oi())

# Exemplo 2


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    if variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Exemplo - Pdoemos, em uma funcao, retornar qualquer tipo de dado e ate mesmo multiplos valores;


def outra_funcao():
    return 2, 3, 4, 5

#num1, num2, num3, num4 = outra_funcao()
#print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar um funcao para jogar a moeda

from random import random


def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1,
    valor = random()
    print(random())
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Erros comuns na utilizacao do retorno, que na verdade nem é erro, mas sim codificação desnecessaria


def eh_impar():
    numero = 61
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
"""

def quadrado_de_7():
    print(7*7)

quadrado_de_7()