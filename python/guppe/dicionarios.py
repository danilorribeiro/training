"""

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

#Acessando elementos (erro caso a chave nao exista)
print(paises['br'])
print(paises['py'])
#Acessando elementos - Recomendada
print(paises.get('br'))
print(paises.get('ru'))

#Encontrando pais com o get
pais = paises.get('py')

pais = paises.get('eua','nao encontrado')

if pais:
    print('encontrei o pais')
else:
    print('nao encontrei o pais')

print(paises)
print(f'Encontrei o pais {pais}')

# Verificando chaves de dicionarios
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

localidades = {
    (35.4564, 39.5464): 'Escritorio em Toquio',
    (40.5465, 74.3040): 'Escritorio em Nova York',
    (37.8731, 122.6874): 'Escritorio em Sao Paulo',
}

print(localidades)
print(type(localidades))

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

receita['abr'] = 350

print(receita)

novo_dado = {'mai': 500}

receita.update(novo_dado)

print(receita)

receita['mai'] = 550

print(receita)

receita.update({'mai': 600})

print(receita)

receita = {'jan': 100, 'fev': 120, 'mar': 300}

ret = receita.pop('mar')
print(ret)

print(receita)

#receita.pop('mar')
del receita['fev']

print(receita)

# Carrinho com lista
carrinho = []

produto1 = ['Playstation', 1, 2300.00]
produto2 = ['Xbox', 1, 1500.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Carrinho com tuplas

produto1 = ('Play4', 1, 2300.00)
produto2 = ('Xbox', 1, 1500.00)

carrinho1 = (produto1, produto2)

print(carrinho)

# Carrinho com dicionario

carrinho2 = []

produto1 = {'nome': 'Play4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'Xbox', 'quantidade': 1, 'preco': 1500.00}

carrinho2.append(produto1)
carrinho2.append(produto2)

print(carrinho2)

# Metodos de dicionarios

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

d.clear()

print(d)
"""

# Copia de dicionario para outro

d = dict(a=1, b=2, c=3)

# forma um deep copy
print(d)

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# forma shallow copy

novo = d

print(novo)

novo['d'] = 5

print(d)
print(novo)
print(type(d))