"""
Utilizando Lambdas

Conhecidas por expressoes Lambdas, ou simplesmente, sao funcoes sem nome, ou seja, funcoes anonimas

# funcao em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressao Lambda


lambda x: 3 * x + 1

# Como utilizar a expressao lambda
calc = lambda x: 3 * x + 1


print(calc(8))

"""

# Podemos ter expressoes lambdas com multiplas entradas


nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


#print(nome_completo(' angel jolie'))
#print(nome_completo(' feliciTY', '   JONES'))

