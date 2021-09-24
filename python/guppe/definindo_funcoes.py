"""
Definincao Funcoes

- Funcoes sao pequenas partes trechos de codigos que realizam tarefas especificas
- Pode ou nao receber entrada de dados e retornar uma saida de dados
- Muito uteis para executar procedimentos similares por repetidas vezes

Ja utilizamos varias funcoes desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- entre outras

"""

# Exemplo de utilizacao de funcoes

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a funcao integrada (Buil-in) do Python print()

# print(cores)

# curso = 'Programacao em Python: Essencial'

# print(curso)

# cores.append('roxo')
# print(cores)

# cores.clear()
# print(cores)

# DRY = Don´t Repeat Yourself - Nao repita voce mesmo / Nao repita seu codigo.

# Mas entao, como definir funcoes?

"""
Em Python, a forma geral de definir um funcao é

def nome_da_funcao(paramentros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome comporto, separado por underline (Snake Case)
paramentros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou nao,
bloco_da_funcao -> Tambem chamado de corpo da funcao ou implementacao, e onde o processamento da funcao acontece.
Neste bloco, pode ter ou nao retorno da funcao

OBS. Beja que para definir uma fucnao, utilizamos a palavra reservada 'def' informando ao Python qu estamos definindo 
uma funcao, Tambem abrimos o bloco de codigo com o ja conhecido dois pontos : que é utilizado em Python para definir 
blocos. 
"""

def diz_oi():
    print('oi!')

"""
OBS.

1 - Veja que, dentro das nossa funcoes podemos utilizar outras funcoes;
2 - Veja que nossa funcao so executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi;
3 - Veja que esta funcao nao recebe nenhum paramentro de entrada;
4 - Veja que esta funcao nao retorna nada;
"""

# Utilizandao funções

# Chamada de execução
diz_oi()

"""
ATENCAO

Nunca se esqueca de utilizar o parenteses ao executar uma funcao

Exemplo:
# ERRADO
diz_oi
diz_oi ()
# CERTO
diz_oi()
"""
def cantar_parabens():
    print('Parabens para voce')
    print('Nesta data querida')
    print('Muitas Felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')
    print('')

#for n in range(5):
#    cantar_parabens()

# Em Python, podemos inclusive criar variaveis do tipo de uma funcao e executar esta funcao atraves da variavel

canta = cantar_parabens

canta()

print(type(canta))
print(type(cantar_parabens()))