"""
List Comprehension

Nos podemos adicionr estruturas condicionais logicas as nossas List Comprehension

"""

# Exemplos

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar
# Qualquer numero par modulo de 2 é 0, e em python é False. not false é True
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)


# 1

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)


