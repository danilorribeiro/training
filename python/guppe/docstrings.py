"""
Documentando funcoes com Docstrings

OBS. Podemos ter acesso a documentacao de uma funcao em Python
utilizando a propriedade especial __doc__

print(help(print))
"""


def diz_oi():
    """Uma funcao simples que retorna a string 'Oi'"""
    return 'Oi'


def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de 'numero' ou o 'numero a potencia 2
    :param numero: numero que desejamos gerar o exponencial
    :param portencia: potencia que queremos gerar o exponencial
    :return: retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia

