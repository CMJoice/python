#Desenvolva um programa que leia as duas notas de um aluno.
#Calcule e mostre a sua média.

nota1 = float(input('primeira nota ' ))
nota2 = float(input('segunda nota '))
media = (nota1 + nota2) / 2
print('com base na nota {} e nota {}, sua media é {}'.format(nota1,nota2,media))