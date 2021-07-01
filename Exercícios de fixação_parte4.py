"""
Exercícios diversos

"""
"""
# 1-Faça um programa que leia um número inteiro e o imprima:


num = 20
print(num)
print(type(num))

#2-Faça um programa que leia um número real e o imprima :

num = -5/2
print(num)
print(type(num))

#3-Peça ao usuário para digitar três valores inteiros e imprima a soma deles :

print('Por favor digite valor1')
valor1 = input()
print('Agora digite valor2')
valor2 = input()
print('Agora digite valor3')
valor3 = input()
res=( int(valor1) + int(valor2) + int(valor3))
print(res)

#4-Leia um número real e imprima o resultado do quadrado desse número :

print('Por favor digite valor : ')
valor = input()
res=(int(valor) * int(valor))
print(res)

#5-Leia um número real e imprima o a quinta parte deste número :
print('Por favor digite valor : ')
valor = input()
res = (int(valor) / 5)
print(res)

#6-Leia a temperatura em graus 'C' e converta 'F', segue formula: F=C * (9.0 / 5.0) + 32.0 :

print('Por favor digite uma temperatura Celsius: ')
temperatura = float(input("O valor é : \n"))
F= (temperatura * (9.0 / 5.0) + 32.0)
print('Resultado da conversão é :\n', F)

#7-Leia em graus 'F' e converte 'C', segue formula: C=5.0*(F - 32.0) / 9.0 :

print('Por favor digite uma temperatura Fahenheit: ')
temperatura = float(input("O valor é : \n"))
C= (5.0*(temperatura - 32.0) / 9.0)
print('Resultado da conversão é :\n', C)

#8-Leia em graus 'K' e converte 'C', segue formula: C= K - 273.15 :

print('Por favor digite uma temperatura Kelvin: ')
temperatura = float(input("O valor é : \n"))
C= (temperatura - 273.15)
print('Resultado da conversão é :\n', C)

#9-Leia em graus 'C' e converte 'K', segue formula: K= C + 273.15 :

print('Por favor digite uma temperatura Celsius: ')
temperatura = float(input("O valor é : \n"))
K= (temperatura + 273.15)
print('Resultado da conversão é :\n', K)

#10-Leia a velocidade em km/h  a apresente em m/s, a formula é : M = K / 3.6 :

print('Por favor digite uma velocidade em km/h: ')
velocidade = float(input("O valor é : \n"))
metros= (velocidade / 3.6)
print('Resultado da conversão é :\n', metros)

#11-Leia a velocidade em m/s  a apresente em km/h, a formula é : K = M * 3.6 :

print('Por favor digite uma velocidade em m/s: ')
velocidade = float(input("O valor é : \n"))
km= (velocidade * 3.6)
print('Resultado da conversão é :\n', km

#12-Leia a velocidade em milhas  a apresente em km/h, a formula é : K = 1.61 * M :

print('Por favor digite uma velocidade em Milhas: ')
velocidade = float(input("O valor é : \n"))
km= ( 1.61 * velocidade)
print('Resultado da conversão é :\n', km)

#13-Leia a velocidade em Km/h  a apresente em Milhas, a formula é : M = k / 1.61:

print('Por favor digite uma velocidade em km/h: ')
velocidade = float(input("O valor é : \n"))
M= ( 1.61 * velocidade)
print('Resultado da conversão é :\n', M)

#14-Leia angulos em graus e converate em radianos , a formula é : R= G * 3.14 / 180 :

print('Por favor digite uma velocidade em graus: ')
graus = float(input("O valor é : \n"))
R= (graus * 3.14 / 180)
print('Resultado da conversão é :\n', R)

#15-Leia em radianos  e converate em graus , a formula é : G= R * 180 / 3.14 :

print('Por favor digite uma velocidade em Radianos: ')
Radianos = float(input("O valor é : \n"))
G= (Radianos * 180 / 3.14)
print('Resultado da conversão é :\n', G)

#16-Leia em polegadas  e converate em  centimetros, a formula é : C= P * 2,54 :

print('Por favor digite uma velocidade em polegadas: ')
polegadas = float(input("O valor é : \n"))
C= (polegadas * 2.54)
print('Resultado da conversão é :\n', C)

#17-Leia em centimetros   e converate em  polegadas, a formula é : P= C / 2.54 :

print('Por favor digite uma velocidade em centimetros: ')
centimetros = float(input("O valor é : \n"))
P= (centimetros / 2.54)
print('Resultado da conversão é : \n', P)

#18-Leia em metros cubicos   e converate em  litros, a formula é : L= 1000 * M :

print('Por favor digite uma velocidade em metros_cubicos: ')
metros_cubicos = float(input("O valor é : \n"))
L= (1000 * metros_cubicos)
print('Resultado da conversão é : \n', L)

#19-Leia em litros    e converate em metros_cubicos , a formula é : M= L / 1000  :

print('Por favor digite uma velocidade em litros: ')
litros = float(input("O valor é : \n"))
M= (litros / 1000)
print('Resultado da conversão é : \n', M)

#20-Leia em Kilograma e converate em Libras , a formula é : L= K / 0.45  :

print('Por favor digite uma velocidade em Kilograma: ')
Kilograma = float(input("O valor é : \n"))
libras= (Kilograma / 0.45)
print('Resultado da conversão é : \n', libras)

#21-Leia em Libras  e converate em Kilograma , a formula é : K= L * 0.45  :

print('Por favor digite uma velocidade em Libras: ')
Libras = float(input("O valor é : \n"))
kilograma= (Libras * 0.45)
print('Resultado da conversão é : \n', kilograma)

#22-Leia em jardas  e converate em metros , a formula é : J = M / 0.91  :

print('Por favor digite uma velocidade em Libras: ')
Libras = float(input("O valor é : \n"))
kilograma= (Libras * 0.45)
print('Resultado da conversão é : \n', kilograma)

#23-Leia em jardas  e converate em metros , a formula é : J = M / 0.91  :

print('Por favor digite uma velocidade em jardas: ')
jardas = float(input("O valor é : \n"))
metros= (jardas / 0.91)
print('Resultado da conversão é : \n', metros)

#24-Leia em metros quadrados  e converate em acres , a formula é : A = M * 0.000247  :

print('Por favor digite uma velocidade em metros_quadrados: ')
metros_quadrados = float(input("O valor é : \n"))
acres= (metros_quadrados * 0.000247)
print('Resultado da conversão é : \n', acres)

#25-Leia em acres   e converate em metros_quadrados, a formula é : M = A * 4048,48  :

print('Por favor digite uma velocidade em acres: ')
acres = float(input("O valor é : \n"))
metros_quadrados= (acres * 0.000247)
print('Resultado da conversão é : \n', metros_quadrados)

#26-Leia em metros_quadrados   e converate em hectares , a formula é : H = M * 0.0001  :

print('Por favor digite uma velocidade em metros_quadrados: ')
metros_quadrados = float(input("O valor é : \n"))
hectares= (metros_quadrados * 0.0001)
print('Resultado da conversão é : \n', hectares)

#27-Leia em hectares e converate em metros_quadrados , a formula é : M = H * 10000  :

print('Por favor digite uma velocidade em hectares: ')
hectares = float(input("O valor é : \n"))
metros_quadrados= (hectares * 10000)
print('Resultado da conversão é : \n', metros_quadrados)

#28-Leia três valores e represente a soma dos quadrados desses valores :

print('Por favor digite o valor1: ')
valor1 = float(input("O valor é : \n"))
valor1= (valor1 * valor1)
print('Por favor digite o valor2: ')
valor2 = float(input("O valor é : \n"))
valor2= (valor2 * valor2)
print('Por favor digite o valor3: ')
valor3 = float(input("O valor é : \n"))
valor3= (valor3 * valor3)
Total = valor1 + valor2 + valor3
print('Resultado da soma dos quadrados dos valores é : \n', Total)

#29-Leia quatro valores e rcalcule a média aritimética e dê o reusltado:

print('Por favor digite o valor1: ')
valor1 = float(input("O valor é : \n"))
print('Por favor digite o valor2: ')
valor2 = float(input("O valor é : \n"))
print('Por favor digite o valor3: ')
valor3 = float(input("O valor é : \n"))
print('Por favor digite o valor4: ')
valor4 = float(input("O valor é : \n"))
Total = (valor1 + valor2 + valor3 + valor4) / 4
print('Resultado da soma dos quadrados dos valores é : \n', Total)

#30-Leia o valor em reais e a cotação do dolar e calcule o valor em dolar:

print('Por favor digite o valor em Reais: ')
Reais = float(input("O valor é : \n"))
print('Por favor digite a cotação do dolar_de_hoje: ')
Cotacao = float(input("O valor é : \n"))
Dolar = Reais / Cotacao
print('Resultado da soma dos quadrados dos valores é :  US$ ', round(Dolar,2))

#31-Leia um numero inteiro e imprima seu antecessor e o seu sucessor:

print('Por favor digite o valor um valor inteiro: ')
num = int(input("O valor é : \n"))
antecessor = num + 1
sucessor = num - 1
print('Resultado do valor inteiro informado :  ', num )
print('Resultado do antecessor :  ', antecessor )
print('Resultado do sucessor :  ', sucessor )

#32-Leia um numero inteiro e imprima a soma de seu sucessor de seu triplo com antecessor de seu dobro:

print('Por favor digite um valor inteiro: ')
num = int(input("O valor é : \n"))
antecessor = num * 3
sucessor = num * 2
print('Resultado do valor inteiro informado :  ', num )
print('O sucessor é :  ',  sucessor)
print('O antecessor é : :  ', antecessor)
print('Resultado da soma  antecessor com o sucessor :  ', antecessor  + sucessor)

#33-Leia um lado de um quadrado e calcule a área :

print('Por favor digite o lado de um quadrado: ')
lado = int(input("O valor é : \n"))
area = lado ** 2
print('A area do quadrado é :  ', area 

#34-Leia o valor do raio de um circulo e calcule a área do circulo, formula = pi * raio², considere pi=3,141592

print('Por favor digite o raio de um circulo:')
raio = int(input("O raio é : \n"))
area = 3.141592 * raio ** 2
print('A area do circulo= ',round(area ,3))

#35-Leia os valores a e b são catetos de um triângulo, onde a hipotenusa é obtida pela equação =
#hipotenusa = √a²+ √b²
import math
print('Por favor digite o cateto A:')
catetoA = int(input("O valor é : "))
print('Por favor digite o cateto B:')
catetoB = int(input("O valor é : "))
hipotenusa = math.hypot(catetoA,catetoB)
print('A hipotenusa do triângulo :',round(hipotenusa,3))

#36-Leia altura e o raio de um cilindro circular e calcule o volume, formula : V = pi * raio² * altura, onde pi = 3,141592

import math
pi = 3.141592
print('Por favor digite o altura:')
altura = int(input("O valor é : "))
print('Por favor digite o raio:')
raio = int(input("O valor é : "))
volume = pi * raio** 2 * altura
print('O volume do cilindro é :',round(volume,3)

#37-Leia o valor do produto e imprima este valor com 12% de desconto:

import math

print('Por favor digite o valor do produto:')
valor = float(input("O valor é : "))
print('Por favor digite percentual de desconto:')
percentual = float(input("O valor é : "))
Valor_final_produto = valor * ((100 - percentual) / 100 )
print('O volume do cilindro é :',round(Valor_final_produto,3))

#38-Leia o valor do salario de um colaborador e imprima o novo_salario com 25% de aumento:

import math

print('Por favor digite o valor do salario:')
salario = float(input("O valor é : "))
print('Por favor digite percentual de aumento:')
percentual = float(input("O valor é : "))
novo_salario = salario * ((100 + percentual) / 100 )
print('O volume do cilindro é :',round(novo_salario,3))

#39-Leia o valor de R$ 780.000.00 será dividida em três, 1-parte receberá: 46%, 2-parte receberá 32% e 3-parte o restante:

import math
print('Por favor digite o valor do premio:')
premio = float(input("O valor é : "))
print('Por favor digite percentual do primeiro recebedor:')
primeiro = float(input("O valor é : "))
print('Por favor digite percentual do segundo recebedor:')
segundo = float(input("O valor é : "))
parte1 = premio * ((100 - primeiro)/100)
parte2 = (premio - parte1) * ((100-segundo) / 100)
parte3 = premio - parte1 - parte2
print('O valor da parte1 é : R$ ',round(parte1,2))
print('O valor da parte2 é : R$ ',round(parte2,2))
print('O valor da parte3 é : R$ ',round(parte3,2))

#40-uma empresa contrata um encanador a R$ 30.00 ao dia, faça um programa que solicite o numero de dias
# trabalhados pelo encanador e informe a quantia_liquida a ser paga já descontados 8% IR:

import math
diaria = 30.00
ir=8
print('Por favor digite os dias_trabalhados:')
dias_trabalhados = float(input("O valor é : "))
quantia_liquida_receber = dias_trabalhados * diaria * ((100 - ir)/100)
print('A quantia liquida a receber é : R$ ',quantia_liquida_receber)

#41-ler hora de trabalho em reais e números de horas trabalhadas no mês, imprima o valor a ser pago
# adcionando  10% do valor calculado:

import math
mes = 30
taxa_adicional=10
dia = 24
print('Por favor digite os valor_hora:')
valor_hora = float(input("O valor é : "))
valor_dia = valor_hora * dia
valor_mês_trabalhado = valor_dia * mes
quantia_liquida_receber = valor_mês_trabalhado * ((100 + taxa_adicional)/100)
print('A quantia liquida a receber é : R$ ',round(quantia_liquida_receber,2))

#42-ler salário base de um funcionário, calcule o salário a receber sabendo que funcionário tem
# uma gratificação de 5% sobre o salario base, é descontado 7% em cima do salário base:

import math
taxa_gratificacao = 5
taxa_desconto= 7
print('Por favor digite os valor do salário:')
valor_salario = float(input("O valor é : "))
valor_salario_gratificacao = valor_salario * ((100 + taxa_gratificacao)/100)
quantia_liquida_receber = valor_salario_gratificacao * ((100 - taxa_desconto)/100)
print('A quantia liquida a receber é : R$ ',round(quantia_liquida_receber,2))

"""

#43-Escreva um progama de ajuda para o vendedor , a partir de um  valor total lido, mostre
# o total a pagar com desconto de 10%; o valor de cada parcela , no parcelamento de 3 x sem juros;
#a comissão do vendedor , no caso da venda ser a vista ( 5% sobre o valor com desconto);
#a comissão do vendedor no caso da venda ser parcelada (5% sobre o valor total)
import math
desc1 =10 #o total a pagar com desconto de 10%;
parc= 3 #sem juros;
com1= 5 #no caso da venda ser a vista sobre o valor com desconto;
com2= 5 #no caso da venda ser parcelada sobre o valor total;

print('Por favor ensira o valor da venda: ')
valor_venda= float(input("Valor é : "))
Total_com_desc= valor_venda * ((100-10)/100)
print('Por favor ensira o número de parcelas: ')
num_parc = int(input("Ensira o numero de parcelas = "))
valor_parcela=Total_com_desc * ((100-10)/100)
com1=(valor_venda * 10/100) * 5/100
com2=Total_com_desc * 5/100
print('O total a pagar com desconto de 10% = ', Total_com_desc  )
print('O número de parcelas da venda até Três vezes sem juros = ', num_parc )
print('A comissão do vendedor  no caso da venda ser a vista =  ',  com1 )
print('A comissão do vendedor no caso da venda ser parceladao =',  com2 )

