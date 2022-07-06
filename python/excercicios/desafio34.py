#Escreva um programa que pergunte o salário de um funcionário
#e calcule o valor do seu aumento.

#Para salários superiores a R$1250,00, calcule um aumento de 10%.

#Para os inferiores ou iguais , o aumento é de 15%.

salário = float(input('informe do funcionario: '))
if salário <= 1250:
  novo = salário + (salário * 15 / 100)
else:
  novo = salário + (salário * 10 / 100)
print('quem ganhava r${:.2f} passa a ganhar {:.2f} agora.'.format(salário,novo))