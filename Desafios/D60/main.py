""" Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor do valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. """

num = int(input('Digite um número: '))
cont = 1
soma = num
continuar = input('Deseja continuar [S/N]: ').upper()
sim = 'S'
não = 'N'
maior = num
menor = num

while continuar == sim:
    num = int(input('Digite outro valor: '))
    continuar = input('Deseja continuar [S/N]: ').upper()
    soma += num
    cont += 1
    if continuar != sim:
        print(f'Média: {soma / cont:.2f}')
    if num > maior:
        maior = num
        print('Maior número: {}'.format(maior))
    if num < menor:
        menor = num
        print('Menor número: {}'.format(menor))
