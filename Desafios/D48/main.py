#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

palin = input('Digite algo: ').lower()

palin = palin.replace(' ', '')

nilap = palin[::-1]

if palin == nilap :
    print('{} é um Palíndromo!'.format(palin))

else:
    print('{} não é um Palíndromo.'.format(palin))