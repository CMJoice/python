#Escreva um programa que leia DOIS NUMEROS 
#inteiros e compare - os, mostrando na tela
#uma mensagem:

#- O primeiro valor é maior.

#- O segundo valor é maior.

#- Não existe valor maior, os dois são iguais.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
  print('O número {} é maior que o {}'.format(n1, n2))
elif n2 > n1:
  print('O número {} é maior que o número {}'.format(n2, n1))
else:
  print('Esses números são iguais.')