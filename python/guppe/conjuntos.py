"""
#Definindo um conjunto

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)
print(type(s))
print(len(s))

s = ({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)
print(type(s))

if 2 in s:
    print('Tem o 2')
else:
    print('nao tem o 2')

lista = [88, 32, 1, 343, 33, 1, 1, 123, 213, 223]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = 88, 32, 1, 343, 33, 1, 1, 123, 213, 223
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([88, 32, 1, 343, 33, 1, 1, 123, 213, 223], 'dict')
print(f'Dicionario:{dicionario} com {len(dicionario)} elementos')

conjunto = {88, 32, 1, 343, 33, 1, 1, 123, 213, 223}
print((f'Conjunto:{conjunto} com {len(conjunto)} elementos'))

lista = [88, 32, 1, 343, 33, 1, 1, 123, 213, 223]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = 88, 32, 1, 343, 33, 1, 1, 123, 213, 223
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([88, 32, 1, 343, 33, 1, 1, 123, 213, 223], 'dict')
print(f'Dicionario:{dicionario} com {len(dicionario)} elementos')

conjunto = {88, 32, 1, 343, 33, 1, 1, 123, 213, 223}
print((f'Conjunto:{conjunto} com {len(conjunto)} elementos'))

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

for valor in s:
    print(valor)

cidades = ['Belo Horizonte', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Sao Paulo', 'Campo Grande']

print(cidades)
print(len(cidades))

s = {1, 2, 3}
s.add(4)
print(s)

s = {1, 2, 3}
print(s)
s.remove(3)
print(s)

s.discard(2)
print(s)

# Deep copy
s = {1, 2, 3}
print(s)

novo = s.copy()
print(novo)

novo.add(4)
print(s)
print(novo)

# Shallow Copy
novo = s
novo.add(4)
novo.add(5)
novo.add(6)
s.discard(3)

print(novo)
print(s)

s.clear()
print(s)

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

unicos2 = estudantes_python | estudantes_java
print(unicos2)

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

ambos1 = estudantes_java & estudantes_python
print(ambos1)

so_phyton = estudantes_python.difference(estudantes_java)
print(so_phyton)
"""

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(min(s))
print(max(s))
print(len(s))