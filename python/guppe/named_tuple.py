from collections import namedtuple

cachorro = namedtuple('cachorro', 'idade raca nome')

cachorro = namedtuple('cachorro','idade, raca, nome')

cachorro = namedtuple('cachorro',['idade','raca','nome'])

ray = cachorro(idade=2, raca="Chow-Chow", nome='Ray')

print(ray)

print(ray[0])
print(ray[1])
print(ray[2])

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))