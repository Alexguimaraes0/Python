""" Crie um algoritimo que leia um número e mostre o seu dobro. triplo e raiz quadrada """
import time


num = int(input('Digite um número:'))

time.sleep(0.5)
print('O dobro é {}! \n o triplo é {}! \n e a raiz quadrada é {}!'.format(num * 2, num * 3, num ** (1/2)))
