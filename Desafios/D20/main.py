#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS.
import math

num = int(input('Digite um número  de 0 a 9999:'))
unidade = num % 10
dezena = num % 100
centena = num % 1000
milhar = num % 10000


print('Analizando o número:{}'.format(num))
print('Unidade:{}'.format(unidade))
print('Dezena:{}'.format(dezena))
print('Centena:{}'.format(centena))
print('Milhar:{}'.format(milhar))