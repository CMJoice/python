#Escreva um programa para aprovar o empréstimo bancário
#para a compra de uma casa.O programa vai perguntar o valor da casa, o salário
#do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode 
#exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? '))
salário = float(input('Quanto é o seu salário? ' ))
anos = float(input('Em quantos anos você pretende pagar a casa? '))
mensalidade = casa / (anos * 12)


if mensalidade > salário * 30/100:
  print('ATENÇÃO! Você excedeu o limite, seu emprestimo está negado! ')
else:
  print('O valor da sua prestação é de: {}, sendo paga em {} anos'.format(mensalidade, anos))
