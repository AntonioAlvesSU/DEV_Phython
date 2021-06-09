"""
Recebendo dados do usuario:
"""
#Entrada de dados
print('Qual seu nome ? ')
nome = input()
#Exemplo de print antigo 2.x
#print('Seja bem-vindo(a) %s' % nome)

#Exemplo de print moderno apartir 3.x
#print('Seja bem-vindo(a) {0}'.format(nome))

#Exemplo de print mais atual 3.7
print(f'Seja bem-vindo(a) {nome}')

print('Qual sua idade? ')
idade = input()

#Processamento

#Saída de dados
#Exemplo de print antigo 2.x
#print('A %s tem %s anos' % (nome, idade)guto)

#Exemplo de print moderno apartir 3.x
#rint('A {0} tem {1} anos'.format(nome, idade))

#Exemplo de print mais atual 3.7
print(f'A {nome} tem {idade} anos')