#um professor quer sortear um dos seus quatro 
#alunos para apagar o quadro.Faça um programa
#que ajude ele, lendo o nome deles e escrevendo 
#o nome do escolhido


from random import choice

n1 = str(input('primeiro nome '))
n2 = str(input('segundo nome '))
n3 = str(input('terceiro mome '))
n4 = str(input('quarto nome '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('o nome escolhido foi {}'.format(escolhido))