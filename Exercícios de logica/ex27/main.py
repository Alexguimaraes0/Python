""" Faça um programa que leia 10 números inteiros e no final mostre:

Quantos números são pares.
Quantos números são ímpares. """


contador = 1
pares = 0
impar = 0

while contador <= 10:
    numero = int(input('Enter a number: '))

    if numero % 2 == 0:
        pares += 1
    else:
        impar += 1

    contador += 1

print('Pares:', pares)
print('Impares:', impar)