#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO

year = int(input('Digite o ano:'))

if (year % 4) == 0:
    print('Bissexto')
else:
    print('Ano Comum')