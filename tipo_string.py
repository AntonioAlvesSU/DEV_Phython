"""
Tipo  string
Em Python , um dado é considerado string sempre que esteiver entre '' simples:
Ex.:
'uma string', '234', 'a', 'True', '42,4'
-sempre que estiver entre "" :
Ex.:
"uma string", "234", "a", "True", "42,4"
-sempre que estiver entre ''' ''' :
Ex.:
'''uma string''', '''234''','''a''', '''True''', '''42,4'''
"""
#-sempre que estiver entre """ """ :Ex.: """uma string""", """234""","""a""", """True""","""42,4"""

#nome ='Antonio Augusto'
nome ='''Antonio Augusto'''
print(nome)
print(type(nome))

nome ="Bob´s Lunch"
print(nome)
print(type(nome))

nome ="Bob´s \nFood"
print(nome)
print(type(nome))

nome ="""Antonio 
Augusto"""
print(nome)
print(type(nome))

nome ='Antonio " Augusto'
print(nome)
print(type(nome))

nome ="Antonio \" Augusto" # Com um caracter de escape você consegue imprimir o resultado com aspas duplas .
print(nome)
print(type(nome))

nome ='antonio augusto'
print(nome.upper())
print(type(nome))

nome ='ANTONIO AUGUSTO'
print(nome.lower())
print(type(nome))

nome ='Antonio  Augusto'
print(nome.split()) #Tranforma em uma lista de string´s
print(type(nome))
"""
 internamente o python transforma o string em uma lista de string´s
 [ 'A','n','t','o','n','i','o',' ','A','u','g','u','s','t','o']
 [  0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13, 14]  
 
 """
nome = 'Antonio Augusto'
print(nome[0:7]) # Slice de string
# Antonio
print(nome[8:15]) # Slice de string
# Augusto
print(nome.split()) # O split transforma o string em duas listas
#['Antonio', 'Augusto']
print(nome.split()[0])
#Antonio
print(nome.split()[1])
#Augusto

#[::-1] -> Comece do primeiro elemento e vá até o ultimo elemento e o inverta
nome ='Antonio Augusto'
print(nome[::-1]) # Inversão da string
print(nome.replace('A', 'D'))
#Dntonio Dugusto
print(type(nome))

Texto ='socorram me subino onibus em marrocos'
print(Texto)
print(Texto[::-1])
"""
socorram me subino onibus em marrocos
socorram me subino onibus em marrocos

palindromo o inverso é o proprio texto
"""




