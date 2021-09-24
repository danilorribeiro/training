"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programacao C/ Java possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes)

Em Python nos temos as Listas

numero = [1, 2, 3, 4, 5]
numero = [1, 'b', 3.234, True, 5] # Em Python pode ser assim

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # comparar uma Matriz 3 x 3

print(listas[0])
print(listas[1])
print(listas[2])
print(type(listas))

print(listas[0][2])
print(listas[2][-1])
print(listas[1][-2])

# Iterando com loops em uma lsita aninhada

for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]
"""

# Gerando um tabuleiro/ matrix 3x3

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1,4)]
print(velha)

# Gerando valor iniciais
print ([['*' for i in range(1, 4)] for j in range(1, 4)])
