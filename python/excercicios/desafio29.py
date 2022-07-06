#escreva um programa que leia a velocidade de um carro. 

#Se ele ultrapassar 80Km/h,mostre uma mensagem dizendo que 
#ele foi multado.

#a multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('digite a velocidade do carro '))
if velocidade > 80:
  multa = (velocidade - 80) * 7
  print('MULTADO!Voce excedeu o limite de 80km/h.')
  print('e deverá pagar multa no valor de R${}'.format(multa))
print('Obrigado por responder!Tenha um bom dia! ')