"""
Tipo Booleano
Algebra Booleana, criado por Geroge Boole
2 constante verdadeiro ou falso

True -> verdadeira
False -> falso

obs.: sempre com a primeira letra maiuscula
"""
#ativo = True
#print(ativo)
#print(type(ativo))


ativo = True
print(ativo)
print(type(ativo))

"""
Operações básicas:
"""
# Negação  (not) :
"""
Fazendo a negação , se o valor booleano for verdadeiro o resultado será falso
se for falso o resultado será verdadeiro
"""
print(not ativo)

# Ou (or)
"""
È uma operação binário, ou seja , um ou putro deve ser verdadeiro
True or True
True
True or False
True
False or False
False
"""
logado = False
print( ativo or  logado)
print(not ativo or  logado)
"""
True
<class 'bool'>
False
True
False
"""

#E (and):
"""
Também é uma opração binária , depende de dois valores e ambos devem ser verdadeiros.

True and True  -> True
True and False -> False
False and False -> True
False
num1 = 4
num2 = 5
num3 = 7
num1 > num2 or num3 > num2
True
num1 > num2 and num3 > num2
False
num1 < num2 and num3 > num2
True


"""






