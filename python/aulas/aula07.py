#OPERADORES ARITMÉTICOS
#adição
#subtração
#multiplicação
#divisão
#potência
#divisão inteira
#resto da divisão

#print('oi'*5)

#print('='*20)

#nome = input('qual é seu nome? ')
#print('prazer em te conhecer{:>20}!'.format(nome))

#nome = input('qual é seu nome? ')
#print('prazer em te conhecer {:^20}!'.format(nome))

n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('a soma é {},o produto é {} e a divisão é {:.3}'.format(s,m,d))
print('divisão inteira {} e potência {}'.format(di,e))