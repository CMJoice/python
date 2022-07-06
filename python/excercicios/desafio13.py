#Faça um algoritmo que leia o salário de um
#funcionário e mostre seu novo salário com 15% de
#aumento

salário = float(input('digite o valor do salário '))
aumento = salário / 100 * 15
salarionovo = salário + aumento
print('o novo salário do funcionário é de {:.2f} reais'.format(salarionovo))

