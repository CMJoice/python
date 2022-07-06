vr = 900
va = 600
salario_rw3 = 2500
salario_jazz = 2400

luz = 100
agua = 60
internet = 120

ganhos = va + vr + salario_rw3 + salario_jazz
dizimo = ganhos / 10

perdas = luz + agua + internet # 100 + 60 + 120
saldo = ganhos - perdas - dizimo


print("o valor da conta de luz é {} reais".format(luz))
print('o valor da conta da agua é {} reais'.format(agua))
print('o valor da conta da internet é {} reais'.format(internet))

print('esse mes voce tem que pagar {} reais'.format(luz + internet + agua))
print('seu ganho é de {} reais e vc devolveu {} de dízimo'.format(saldo, dizimo))

print('voce recebeu {} reais de vr e {} reais de va'.format(vr,va))

# print('qual o nome do seu marido?')
# marido = input('qual o nome do seu marido?\n')

# print('O nome do seu marido é {}, correto?'.format(marido))








cadeira = 1500
print('o valor da cadeira é de {} reais'.format(float(cadeira)))

