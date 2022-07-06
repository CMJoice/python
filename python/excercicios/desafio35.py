#Desenvolva um programa que leia o comprimento de três
#retas e diga ao usuário se elas podem ou não formar
#um triângulo.

r1 = float(input('primeiro numero: '))
r2 = float(input('segundo numero: '))
r3 = float(input('terceiro numero: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('os segmentos acima PODEM FORMAR triângulo!')
else:
  print('os segmentos acima NÃO PODEM formar triângulo!')