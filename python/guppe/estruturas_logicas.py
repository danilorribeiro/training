"""
Estruturas logicas,
operadores unarios
    not, is

    'not' o valor do booleano é invertido, se for True vira False, se for False vira True

operadores binarios
    and,or

    'and' ambos as condicoes precisam ser True
    ´or´ um ou outra condicao preccisa se True
    
    
tabela de unicode
https://apps.timwhitlock.info/emoji/tables/unicode 
""""

ativo = False
logado = True

if ativo:
    print('Bem vindo usuario')
else:
    print('Voce precisa ativar sua conta. Por favor check seu email')

print(ativo is True)
"""