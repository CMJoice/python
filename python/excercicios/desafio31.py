#Desenvolva um programa que pergunte a distância
#de uma viagem em Km.Calcule o preço da passagem, 
#cobrando R$0,50 por Km para viagens de até 200 Km
# e R$0,45 para viagens mais longas.

distância = float(input('Olá, me informe a distância da sua viagem: '))
print('Você está para fazer uma viagem de {}Km.'.format(distância))
if distância <=200:
  preço = distância * 0.50
else:
  preço = distância * 0.45

print('O preço de sua passagem será de: {:.2f} reais'.format(preço))
