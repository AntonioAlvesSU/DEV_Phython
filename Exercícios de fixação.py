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

#15-Leia angulos em graus e converate em radianos , a formula é : R= G * 3.14 / 180 :

print('Por favor digite uma velocidade em graus: ')
graus = float(input("O valor é : \n"))
R= (graus * 3.14 / 180)
print('Resultado da conversão é :\n', R)

"""
#15-Leia radianos em graus e converate em graus , a formula é : G= R * 180 / 3.14 :

print('Por favor digite uma velocidade em Radianos: ')
Radianos = float(input("O valor é : \n"))
G= (Radianos * 180 / 3.14)
print('Resultado da conversão é :\n', G)





















