"""
Funcoes com Paramentro(de entrada)

- Funcoes que recebem dados para serem processador dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

Se a gente pensar em uma funcao, ja sabemos que temos funcoes que:
- Nao possuem entrada;
- Nao possuem saida;
- Possuem entrada mas nao possuem saida;
- Nao possuem entrada mas possuem saida;
- Possuem entrada e saida


# Refatorando uma funcao

def quadrado(numero):
    #return numero * numero
    return numero ** 2

print(quadrado(2))
print(quadrado(7))
print(quadrado(5))


def cantar_parabens(aniversariante):
    print('Parabens para voce')
    print('Nesta data querida')
    print('Muitas Felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')
    print('')


cantar_parabens('Patricia')

# Funcoes podem ter n parametros de entrada. ou seja, podemos recebe como entrada.
# em um funcao quantos paramentros forem necessarios. Eles sao separados por virgula

# Exemplos

def soma(a, b):
    return a + b


def multiplica(num1,num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10,20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(2, 1, 'Python '))

# OBS: Se a gente informar um numero errado parametro ou argumentos, teremos TypeError
"""


def nome_completo (nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angeline', 'Jolie'))

# A diferenca entre Paramentro e Argumentos

# Paramentros sao variaveis declaradas na definicao de uma funcao;
# Argumentos sao dados passados durante a execucao de uma funcao

# A ordem dos parametros importa

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parametros nos argumentos para informa-los, podemos utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

# Erro comum na utilizacao do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))
