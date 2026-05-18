#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS
import time

m = float(input('Quantos metros você correu?:'))

print('Convertendo...')

time.sleep(2)

c = m * 100

print('Você correu {:.0f} Centimetros!'.format(c))

time.sleep(0.5)

print('Convertendo...')

time.sleep(2)

mm = m * 1000

print('Você correu {:.0f} Milimetros!'.format(mm))