#Crie um programa que leia um número real qualquer pelo 
#teclado e mostre na tela a sua porção inteira.

#real = float(input('digite um número, por favor '))
#print('o valor digitado foi {} e sua porção inteira é {}'.format(real,int(real)))

#import math

#real = float(input('digite um valor '))

#print('o valor digitado foi {} e sua porção inteira é {}'.format(real, math.floor(real)))

#import math

#num = float(input('digite um número: '))
#print('o valor é {} e sua porção inteira é de {}'.format(num, math.ceil(num)))

#import math

#numero = float(input('digite um valor: '))
#print('o valor digitado foi {} e sua porção inteira é {}'.format(numero, math.floor(numero)))

from math import trunc

num = float(input('digite um valor '))
print('o valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))