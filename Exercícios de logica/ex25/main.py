""" Faça um programa que leia 5 números inteiros e mostre:

Qual foi o maior número digitado.
Qual foi o menor número digitado.
A soma de todos os números. """

num1 = int(input('Digite os números:'))
num2 = int(input('Digite os números:'))
num3 = int(input('Digite os números:'))
num4 = int(input('Digite os números:'))
num5 = int(input('Digite os números:'))

print(num1)
print(num2)
print(num3)
print(num4)
print(num5)

print('-'* 10)

print('Maior número: {}'.format(max(num1, num2, num3, num4, num5)))
print('Menor número: {}'.format(min(num1, num2, num3, num4, num5)))
print('Soma de todos eles: {}'.format(num1 + num2 + num3 + num4 + num5))