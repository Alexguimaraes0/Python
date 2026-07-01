""" O usuário informa um valor inteiro (ex.: R$ 286).
O programa deve dizer quantas notas serão entregues. """

valor = int(input('Valor: '))

print(f'Valor: R${valor}')

notas100 =valor // 100
valor = valor % 100

notas50 =valor // 50
valor = valor % 50

notas20 = valor // 20
valor = valor % 20

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas1 = valor // 1

nota = notas100, notas50, notas20, notas10, notas5, notas1

if notas100 == 1:
    print(f'{notas100} nota de R$100')
else:
    print(f'{notas100} notas de R$100')
if notas50 == 1:
    print(f'{notas50} nota de R$50')
else:
    print(f'{notas50} notas de R$50')
if notas20 == 1:
    print(f'{notas20} nota de R$20')
else: 
    print(f'{notas20} notas de R$20')
if notas10 == 1:
    print(f'{notas10} nota de R$10')
else:
    print(f'{notas10} notas de R$10')
if notas5 == 1:
    print(f'{notas5} nota de R$5')
else:
    print(f'{notas5} notas de R$5')
if notas1 == 1:
    print(f'{notas1} nota de R$1')
else:
    print(f'{notas1} notas de R$1')