""" Faça um programa que pergunte quantos números o usuário deseja digitar. Em seguida, leia todos os números e mostre qual foi o maior. """

quantidade = int(input('Quantos números? '))

maior = 0

for c in range(quantidade):
    num = int(input('Número: '))

    if c == 0:
        maior = num
    elif num > maior:
        maior = num

print(f'Maior número: {maior}')