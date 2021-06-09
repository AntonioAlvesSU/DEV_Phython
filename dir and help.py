"""
Utilitarios Python para auxiliar na programação :
dir -> Apresenta todos os atributos e funções e metodos disponiveis para tipo de dado ou variavel.
dir(tipo de dado ou cariavel)
help -> Apresnta a documentação / como utlizar os atributos/propriedades e funções e metodos disponíveis para
determindao tip de dado ou variável
(c) Microsoft Corporation. Todos os direitos reservados.

(Desenvolvimento) C:\Users\GUTO\PycharmProjects\aula\Desenvolvimento>python
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
#>>> "GOD IS MY LORD"
'GOD IS MY LORD'
#>>> print('
  File "<stdin>", line 1
    print('
          ^
SyntaxError: EOL while scanning string literal
#>>> print('GOD IS MY LORD')
GOD IS MY LORD
#>>> 4 + 5
9
#>>> dir('GOD')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_
ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswi
th', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprint
able', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#>>> help("GOD".lower)
Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.

#>>> "GOD".lower()
'god'
#>>> "GOD".upper()
'GOD'
#>>> help("GOD".upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

#>>> help("desenvolvimento".tittle)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'tittle'
#>>> help("desenvolvimento".title)
Help on built-in function title:

title() method of builtins.str instance
    Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining
    cased characters have lower case.

#>>> "desenvolvimento".title()
'Desenvolvimento'
#>>> 'antonio augusto'.title()
'Antonio Augusto'
#>>> 'ANTONIO AUGUSTO'.lower().title()
'Antonio Augusto'
#>>> 4 + 5
9
#>>> dir(4)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floo
rdiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '
__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__redu
ce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub_
_', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bi
t_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
#>>> num = 4
#>>> num
4
#>>> num.__add__(6)
10
#>>> num + 6
10
#>>>

"""
