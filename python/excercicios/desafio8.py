#Escreva um programa que leia um valor em metros
#e o exiba convertido em centimetros e milimetros.

n = float(input('digite um valor em metros '))
m = n * 100
cm = n * 1000
print('a distância de {} é de {} metros '.format(n,m))
print('a distancia de {} é de {} centimetros'.format(n,cm))