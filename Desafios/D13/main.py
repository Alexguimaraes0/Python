#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA
from math import trunc

num = float(input('Digite um número:'))

print(f'O número:{trunc(num)}')