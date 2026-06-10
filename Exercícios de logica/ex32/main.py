#Faça um programa que peça um número inteiro ao usuário e mostre a tabuada desse número de 1 a 10 usando "for".

num = int(input('Digite um número de 1 a 10: '))

for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, num * c))