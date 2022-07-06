#Faça um programa que leia a largura e a altura dPintando Paredee uma
#parede em metros. Calcule a sua área e a quantidade da 
#tinta necessária para pintá-la,sabendo que cada litro da 
#tinta pinta uma área de 2m².

# [X] - ler a altura em metros
# [X] - ler a largura em metros
# [X] - calcular a área - L * A
# [] - calcular o rendimento da tinta

altura = float(input('Digite a altura de sua parede '))
largura = float(input('Agora,digite a sua largura '))
área = altura * largura #M²
tinta = área / 2
print('sabendo que a área é de {}m², você precisará de {} litros de tinta para pintar a parede.'.format(área,tinta))