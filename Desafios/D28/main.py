#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM Km.Calcule o preço da passagem, cobrando R#0,50 por Km para viagens de até
#200Km e R$0,45 PARA VIAGENS MAIS LONGAS
import os
os.system('cls')

km = float(input('Ensira a distancia:'))


if km <= 200:
    print('Cobrança dentro do Limite de 200Km:{}'.format(km * 0.50))
else:
    print('Cobrança passando o Limite de 200Km:{}'.format(km * 0.45))