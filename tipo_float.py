""""
Tipo float

Tipo real, decimal

casas decimais é o 'ponto e não a virgula'
(1, 44)
<class 'tuple'>
1.44
<class 'float'>

# E possivel fazer dupla atribuição
1
<class 'int'>
44
<class 'int'>

1j
1j
5j
5j
type(5j)
<class 'complex'>
variavel = 5j
type(variavel)
<class 'complex'>
variavel ** 2
(-25+0j)
variavel ** -2
(-0.04-0j)
"""

#Errado do ponto de vista do float , mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))
# Certo do ponto de vista float
valor =1.44
print(valor)
print(type(valor))

# E possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#Podemos converter uma float para um int
"""
OBS.: Ao fazermos um cast de um 'float' para 'int' nós perdemos precisão .
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j

num = 100_000
print(num)
print(float(num))


