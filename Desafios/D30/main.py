#FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR

num1 = int(input('Insira um Número: '))
num2 = int(input('Insira um Número: '))
num3 = int(input('Insira um Número: '))

maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

'====================='

menor = num1

if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

print('Maior:{}'.format(maior))
print('Menor:{}'.format(menor))