#faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo. Calcule
#e mostre o comprimento da hipotenusa.

#from math import hypot

#adjacente = int(input('informe o valor do cateto adjacente '))
#oposto = int(input('informe o valor do cateto oposto '))
#hipotenusa = hypot(adjacente, oposto)
#print('o valor do cateto adjacente é {} e o cateto oposto é {} e o valor da hipotenusa\né {:.2f}'.format(adjacente,oposto,hipotenusa))


from math import hypot

co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))
hi = hypot(co, ca)

print('a hipotenusa é {:.2f}'.format(hi))