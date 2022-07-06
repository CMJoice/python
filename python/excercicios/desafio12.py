#Faça um algoritmo que leia o preço de um produto
#e mostre seu novo preço com %5 de desconto.

produto = float(input('digite o valor do produto' ))
desconto = produto / 100 * 5
novopreço = produto - desconto
print('o novo preço do produto é {} reais'.format(novopreço)) 

