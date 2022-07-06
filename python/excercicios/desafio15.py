#escreva um programa que pergunte a quantidade de KM percorridos
#por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e 
# R$0,15 por Km rodado. 

km = float(input('qual a quantidade de km rodado? '))
dias = int(input('por quantos dias o carro foi alugado? '))
preço = (60.00 * dias) + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(preço))