#faça um programa que leia um ângulo qualquer
#e mostre na tela o valor do seno,cosseno e  
#tangente desse ângulo.

#from math import sin,cos,tan

'''n = int(input('digite um ângulo '))
seno = sin(n)
cosseno = cos(n)
tangente = tan(n)
print('considerando que o ângulo é {},\nlogo o valor do seno é {},\ndo cosseno é {} e de sua tangente é {}'.format(n,seno,cosseno,tangente))'''


#import math

#ângulo = float(input('digite o ângulo que você deseja: '))
#seno = math.sin(math.radians(ângulo))
#print('o ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
#cosseno = math.cos(math.radians(ângulo))
#print('o ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
#tangente = math.tan(math.radians(ângulo))
#print('o ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

from math import radians, sin, cos, tan

ângulo = float(input('digite o ângulo: '))
s = sin(radians(ângulo))
c = cos(radians(ângulo))
t = tan(radians(ângulo))
print('SENO é {:.2f}'.format(s))
print('COSSENO é {:.2f} '.format(c))
print('TANGENTE é {:.2f}'.format(t))
