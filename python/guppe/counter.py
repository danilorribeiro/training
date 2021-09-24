"""
from collections import Counter

lista = [1, 1, 1, 1, 2, 3, 3, 3, 5, 4, 4, 4, 5, 5, 5, 45, 45, 45, 66, 45, 43, 34]

res = Counter(lista)

print(type(res))

print(res)

print(Counter('Geek University'))

"""

from collections import Counter

texto = """Acrocantossauro é um gênero de um dinossauro terópode que existiu onde hoje é a América do Norte durante 
os períodos Aptiano e Albiano do período Cretáceo Inferior, aproximadamente 125 a 100 milhões de anos atrás. Como a
 maioria dos gêneros de dinossauro, o Acrocanthosaurus possui apenas uma espécie, A. atokensis. Os restos de seus 
 fósseis se encontram principalmente nos estados de Oklahoma, Texas e Wyoming (Estados Unidos), apesar de dentes 
 atribuídos a ele terem sido encontrados, a grande distância ao leste, em Maryland.
Acrocanthosaurus foi um predador bípede. Como o nome sugere, ele é bem conhecido pela grandes espinhas em muitas 
de suas vértebras, que provavelmente apoiaram os músculos do animal ao longo do pescoço, costas e quadris. 
O Acrocanthosaurus foi um dos maiores terópodes podendo chegar a 3,5 metros de altura, aproximando-se dos 11,
5 metros de comprimento (38 pés), e pesando até cerca de 6,2 toneladas. Grandes pegadas feitas por terópodes 
encontradas no Texas podem ser de Acrocanthosaurus, embora não tenha sido encontrada ligação direta com restos 
ósseos."
"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

# print(res)

print(res.most_common(5))
