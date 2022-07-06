#faça um programa que leia um numero de 0 a 9999 e 
#mostre na tela cada um dos dígitos separados.
#EXEMPLO:1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1

numero = int(input('informe um numero '))
uni = numero// 1 % 10
dez = numero// 10 % 10
cen = numero// 100 % 10
mil = numero// 1000 % 10
print('analisando o valor {}'.format(numero))
print('sua unidade é {}'.format(uni))
print('sua dezena é {}'.format(dez))
print('sua centena é {}'.format(cen))
print('seu milhar é {}'.format(mil))
