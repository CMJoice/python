#escreva um programa que faça o computador "pensar"
#em um numero inteiro entre 0 e 5 e peça para o 
#usuario tentar descobrir qual foi o numero escolhido
#pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou
#perdeu.

#from random import randint
#from time import sleep
#computador = randint(0, 5)
#print('vou pensar em um numero de 0 a 5, tente adivinhar... ')
#sleep(5)
#jogador = int(input('o numero em que pensei foi? '))
#print('PROCESSANDO...')
#sleep (5)
#if jogador == computador:
  #print('Parabens!Voce venceu!')
#else:
  #print('ERROU! Eu pensei no numero {} e não no {}.'.format(computador, jogador))
  #print('tente novamente!')

from random import randint
from time import sleep

computador = randint(0,10)
print('Vou pensar em um número de 0 a 10, tente adivinhar: ')
sleep(4)
jogador = int(input('Qual o número que pensei? '))
print('PROCESSANDO...')
sleep(4)
if jogador == computador:
  print('Parabéns! Você venceu!!! ')
else:
  print('Errou! Eu pensei no número {} e não no {}'.format(computador,jogador))
  print('Tente novamente! ')





