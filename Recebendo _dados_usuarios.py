"""
Recebendo dados do usuario:
input() -> Todo dado recebido via input é do tipo string
Tudo que estiver entre :
-Aspas simples
-Apas duplas
_Aspas simples triplas
-Aspas duplas triplas
exemplo:
-Aspas simples-> 'guto'
-Apas duplas-> "guto"
_Aspas simples triplas-> '''guto'''
"""
#-Aspas duplas triplas->"""guto"""
""""
#Entrada de dados
print('Qual seu nome ? ')
#nome = input()
#Exemplo de print antigo 2.x
#print('Seja bem-vindo(a) %s' % nome)

#Exemplo de print moderno apartir 3.x
#print('Seja bem-vindo(a) {0}'.format(nome))

#Exemplo de print mais atual 3.7
#print(f'Seja bem-vindo(a) {nome}')

#print('Qual sua idade? ')
#idade = input()

#Processamento

#Saída de dados
#Exemplo de print antigo 2.x
#print('A %s tem %s anos' % (nome, idade)guto)

#Exemplo de print moderno apartir 3.x
#rint('A {0} tem {1} anos'.format(nome, idade))

#Exemplo de print mais atual 3.7
#print(f'A {nome} tem {idade} anos')
#int(idade) => cast
#Cast é a conversão de um tipo de dado para outro.
"""
#Entrada de dados
#print('Qual seu nome ? ')
#nome = input()
nome = input('Qual seu nome ? ')

print(f'Seja bem-vindo(a) {nome}')


#print('Qual sua idade? ')
#idade = input()
#idade = input('Qual sua idade ? ')
idade = int(input('Qual sua idade ? '))

print(f'A {nome} nasceu em {2021 - idade}')