"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python
The Zen of Python
import this -comando par ester eggo
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
################################################################################
A idéia da PEP8 para que possamos escrever os códigos de forma Phythonica.
[1] - Utilize o Camel case para nomes de classes;
class Calcualdora:
    pass

class CalcualdoraCientifica:
    pass

[2] - Dê dois espaços em linha por código;
    - Métodos dentro de uma classe devem ser separados com uma linha em branco;

class Classe:
    pass

class Objeto:
    pass

[3] - Utlçize nomes em minusculos, separados por unederline para funções ou variaveis;
def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar  = 5

[4] - Utlize quatro espaços para identação, não use tab.
if 'a' in 'banana':
    print('tem')

[5] - Imports : devem ser sempre feitos em linhas separadas;
#Errado
import sys,  os
#import Certo
impor sys
import os
#Não há problema em utilizar PARA IMPORTAR ALGUMAS CLASSES DE UM IMPORT:
from types import StringType, ListType
#CASO TENHA MUITOS IMPORTS DE UM MESMO PACOTE, RECOMENDA-SE:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)
#Imports devem ser colocados no topo do arquivo,logo depois de quaisquer comentários ou docstrings e
#antes de constantes ouy variáveis globais,

[6] - espaços em expressoes e instruções
#Não faça :
funcao(_algo[_1_], {_outro: 2_}_)
#faça:
funcao(algo[1], {outro: 2})
#não faça:
algo_(1)
#faça:
algo(1)
#não faça:
dict ['chave'] = list_[indice]
#faça:
dict['chave'] = list[indice]
#não faça :
x_____________ = 1
y_____________ = 3
variavel_longa = 5
#faça:
x = 1
y = 3
variavel_longa = 5
[7] - Termine sempre uma instrução com uma nova linha:

import this

"""














