#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
#CONSIDRE 1US$ = R$ 3,27
import time

valor = float(input('Quantos R$ você tem?: R$'))
dolar = valor / 3.27

print('Convertendo...')

time.sleep(2)

print(f'Com R${valor:.2f} você pode comprar U${dolar:.2f} dolares')