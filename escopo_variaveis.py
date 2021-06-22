"""
Escopo de variáveis
/                / limiação de espaço dentro de um programa
Existem dois casos de escopos:
1- Variáveis Globais-> são reconhecidas em todo o programa.
2- Variáveis locais-> são reconhecidas dentro do bloco onde foi declarada.

Para declarar variaveis em Python fazemos
nome_da_variavel = valor_da_variavel
Pythom é uma linguagem de tipagem dinâmica . ao declararmos uma variável , não colocamos o  tipo dela.
Este tipo é inferido ao atribuírmos o valor à mesma

Ex. em C:
int num = 42

Ex.: em Java:
int num = 42

no Python podemos fazer a reatibuição do dado

"""
num = 42 # Exemplo de variável global
print(num)
print(type(num))

num = 'Antonio'
print(num)
print(type(num))
"""
num = 42

if num > 10:
    novo = num + 10
    print(novo)
    52
"""
num = 2

if num > 10:
    novo = num + 10
    print(novo) # Este valor não existe porque não atendeu a condicional/ faz parte de escopo local

num = 2
novo = 0

if num > 10:
    novo = num + 10
    print(novo) # Este valor não existe porque não atendeu a condicional/ faz parte de escopo local declarada
# No escopo do if
print(novo) # Nete caso foi declarada como Global.


