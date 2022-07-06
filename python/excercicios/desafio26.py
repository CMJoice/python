#faça um programa que leia uma frase pelo
#teclado e mostre: 

#Quantas vezes aparece a letra "A".

#Em que posição ela aparece a primeira vez.

#Em que posição ela aparece a segunda vez.

frase = str(input('digite a frase ')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('a ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))


#frase = str(input('digite a frase '))
#print('a primeira letra a aparece na posição {}'.format(frase.find('a')))
#print('a ultima letra a aparece na posiçao {}'.format(frase.rfind('a')))