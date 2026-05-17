#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
#CONSIDRE 1US$ = R$ 3,27
import time

valor = float(input('Quantos R$ você tem?:'))

print(valor)

print('Convertendo...')

time.sleep(2)

print(round(valor / 3.27),)