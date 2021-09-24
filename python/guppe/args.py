"""
Entendendo o *args

- o *args e um paramentro, como outro qualquer, Isso significa que voce podera
chamar de qualquer coisa, dese que comece com asterisco.

Exemplo:

*xis

Mas por convencao, utilizamos *args para defini-lo

Mas o que é o *args?

O parametro *args utilizado em uma funcao, coloca os valors extras informados como
entrada em uma tupla. Entao desde ja lembre-se que tuplas sao imutaveis.


def soma_total(num1, num2, num3):
    return num1 + num2 + num3


print(soma_total(2, 4, 5))


def soma_args(nome, email, *args):
    return sum(args)


print(soma_args('Angelina', 'ddd@ddd'))
print(soma_args('Angelina', 'ddd@ddd', 1))
print(soma_args('Angelina', 'ddd@ddd', 2, 3))
print(soma_args('Angelina', 'ddd@ddd', 3, 4, 5))
print(soma_args('Angelina', 'ddd@ddd', 5, 6, 7, 8))
print(soma_args('Angelina', 'ddd@ddd', 23.4, 55.9))

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Nao sei quem vc e'

print(verifica_info())
print(verifica_info(1, True,'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

"""


def soma_todos(*args):
    return sum(args)


print(soma_todos())
print(soma_todos(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 55]    # funciona com lista, tupla e set

print(soma_todos(*numeros))
