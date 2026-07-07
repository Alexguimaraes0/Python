""" Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso." """
import time

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
numero_maior = 0

while True:

    print('=' * 20)
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior')
    print('4 - Novos números')
    print('0 - Sair')

    escolha = int(input('Escolha:'))

    if escolha == 1:
        print('A soma de {} + {} é: {}'.format(num1, num2, num1 + num2))
        
    
    elif escolha == 2:
        print('A multiplicação de {} X {} é: {}'.format(num1, num2, num1 * num2))
        
    elif escolha == 3:
        if num1 > num2:
            numero_maior = num1
        if num2 > num1:
            numero_maior = num2
            print('O maior número entre eles é o {}'.format(numero_maior))
            
    elif escolha == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif escolha == 0:
        print('Fechando o Menu...')
        time.sleep(0.8)
        break
    


    
