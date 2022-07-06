#crie um programa que leia o nome de uma 
#cidade e diga se ela começa com a palavra "Santo".

#frase = input('digite o nome da cidade: ')
#print(frase.find('SANTO'))
#print('Santo'in frase) 

cid = str(input('em que cidade você nasceu '))
print(cid[:5].upper() == 'SANTO') 