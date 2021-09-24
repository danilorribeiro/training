"""
Funcoes com Parametro Padrao (default Parameters)

- Funcoes onde a passagem de parametro seja opcional

# Exemplo de funcao onde a passagem de parmetro seja opcional

print('Geek University')

print()

# Exemplo de funcao onde a passagem de erro e obrigatoria
def quadrado(numero):
    return numero ** 2

print(quadrado(3)) # passagem de valor obrigatorio
print(quadrado())  # apresenta erro TypeError


def exponencial(numero=0, potencia=2):
    return numero ** potencia


print(exponencial(2, 4))
print(exponencial(3, 4))

print(exponencial(0, 2))     #

# OBS: Em funcoes python , os parametros com valores default(padrao)
# DEvem sempre estar ao final da declaracao
# ERRO!
def teste(potencia, num=2)
    return num ** portencia


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem bindo instrutor Geek!'
    if nome == 'Geek':
        return 'Eu pensei que voce era o instrutor'
    return f'Ola {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephan'))

# Por que utilizar parametros com valor default?

- Nos permite ser mais flexiveis nas funcoes
- Evita erros com parametro incorretos
- Nos permite trabalhar com exemplos mais legiveis de codigo


# Quais tipos de dados podemos utilizar como valores default para parametros

- Qualquer tipo de dado:
     - Numeros, strings, floats, booleanos, listas, tuplas, funcoes, etc

# Exemplos


def somador(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=somador):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))
# Escopo - Evitar problemas e confusoes

# Variaveis globais
# Variabeis locais

# Se tivermos uma variavel local com o mesmo nome da variavel global, era sera utilizada


def diz_oi():
    instrutor = 'Python'
    return f'Oi {instrutor}'

print(diz_oi())

instrutor = 'Geek' #Variavel global


def diz_oi():
    prof = 'Geek'
    return f'Oi {prof}'

print(diz_oi())

print(prof)  #NameError


# ATENCAO com variaveis globais (se puder evitar, evite)


total = 0


def incremeta():
    global total
    total = total + 1
    return total

print(incremeta())

"""


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())