#crie um programa que leia quanto dinheiro tem na carteira 
#e mostre quantos dólares ele pode comprar.Considere: USS1.00 = R$3.27

carteira = float(input('o cara tem quanto na carteira? '))
dólar = carteira / 3.27
print('Com {} reais, o cara pode comprar {:.2f} de dolares'.format(carteira,dólar))
