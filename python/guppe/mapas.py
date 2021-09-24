"""
print(receita)

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

print(receita.values())

for valor in receita.values():
    print(valor)

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
