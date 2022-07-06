#crie um programa que leia o nome de uma pessoa e
#diga se ela tem "SILVA" no nome.

frase = input('digite seu nome: ').strip()
print('seu nome tem Silva? {}'.format('silva' in frase.lower()))