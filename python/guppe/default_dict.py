"""
Modulo Default Dict
# Recap Dicionarios

dicionario = {'curso':'Priogramacao em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

"""

from collections import defaultdict

dicionario = defaultdict(lambda: 0)


dicionario['curso'] = 'Programacao em Python: Essencial'

print(dicionario)

print(dicionario['outro'])

print(dicionario)
