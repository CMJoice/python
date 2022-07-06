#CORES NO TERMINAL
#padrão ANSI, escape sequence

#para adicionar cor ao terminal sempre se inicia com:
#\033[m

#exemplo:
#\033[0;33;44m
#style(estilo) / text(cor) / back (cor de fundo)

#STYLE:
#0  None  (sem estilo)
#1  Bold  (negrito)
#4  Underline (sublinhado)
#7  Negative  (inverte configuração)

#TEXT:
#30 Branco
#31 Vermelho
#32 Verde
#33 Amarelo
#34 Azul
#35 Roxo
#36 Ciano
#37 Cinza

#BACK:
#40 Branco
#41 Vermelho
#42 Verde
#43 Amarelo
#44 Azul
#45 Roxo
#46 Ciano
#47 Cinza

#print('\033[7;33;44mOlá Mundo!\033[m')

a = 3
b = 5
print('os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a,b))