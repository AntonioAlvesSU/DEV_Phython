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

"""
#30-Leia o valor em reais e a cotação do dolar e calcule o valor em dolar:

print('Por favor digite o valor em Reais: ')
Reais = float(input("O valor é : \n"))
print('Por favor digite a cotação do dolar_de_hoje: ')
Cotacao = float(input("O valor é : \n"))
Dolar = Reais / Cotacao
print('Resultado da soma dos quadrados dos valores é :  US$ ', round(Dolar,2))





















