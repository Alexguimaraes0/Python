""" Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. """

valor = 1
valor_digitado = 1
cont = 0

while valor_digitado != 0:
    print('=' * 20, 'Banco', '=' * 20)
    valor = int(input("Insira o valor desejado: "))
    valor_digitado = valor

    nota50 = valor // 50
    valor = valor % 50


    nota20 = valor // 20
    valor = valor % 20


    nota10 = valor // 10
    valor = valor % 10


    nota1 = valor // 1
    valor = valor % 1

    if nota50 > 0:
        print(f'Total de {nota50} cédulas de R$50')

    if nota20 > 0:
        print(f'Total de {nota20} cédulas de R$20')
        
    if nota10 > 0:
        print(f'Total de {nota10} cédulas de R$10')
        
    if nota1 > 0:
        print(f'Total de {nota1} cédulas de R$1')

    print('=' * 40)

    print("Volte sempre ao nosso BANCO! Tenha um Bom dia!")
    break