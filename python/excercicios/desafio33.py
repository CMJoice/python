#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('digite o primeiro número: '))
b = int(input('digite o segundo número: '))
c = int(input('digite o terceiro número: '))
#verificando o menor
menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c
#verificando o maios
maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c 
print('o menor valor digitado foi: {}'.format(menor))
print('o maior valor digitado  foi:{}'.format(maior))
