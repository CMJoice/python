#o mesmo professor do desafio anterior quer  
#sortear a ordem de apresentação de trabalhos
#dos alunos.Faça um programa que leia o nome 
#dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('primeiro nome ')) 
n2 = str(input('segundo nome '))
n3 = str(input('terceiro nome '))
n4 = str(input('quarto nome '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('a ordem é {}'.format(lista))
