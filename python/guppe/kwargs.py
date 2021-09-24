"""
**kwargs


# obs. Os parametros *args ou **kwargs nao sao obrigatorios

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo',fernanda='azul', vanessa='branco')
cores_favoritas(geek='navy')

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Nao tenho certeza de quem vc é'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossa funcoes, podemos ter(NESTA ordem):

- Parametros obrigatorios;
- *args;
- Parametros default (nao obrigatorios);
- **kwargs;


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Nao', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Funcao com a ordem CORRETA de parametros
def mostra_info(a,b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


# Funcao com a ordem CORRETA de parametros
#def mostra_info(a,b, instrutor='Geek', *args, **kwargs):
#    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotando com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))


"""


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)


# soma_multiplos_numeros(1, 2 ,3)
lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = ({1, 2, 3})
dicionario = dict(a=1, b=2, c=3)
dicionariodif = dict(c=1, d=2, f=3) #TypeError
# OBS. os nome da chave em um dicionario deve ser o mesmo da funcao

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario)

soma_multiplos_numeros(**dicionario, lang='Python')
