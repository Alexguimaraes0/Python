""" Crie um programa que simule um caixa eletrônico simplificado. O programa deve perguntar ao usuário o valor que ele deseja sacar. Sabendo que o caixa só possui notas de
 R$50, R$20, R$10 e R$5, o programa deve informar quantas notas de cada tipo serão 
 entregues, usando a menor quantidade de notas possível. O programa deve repetir o processo
 até que o usuário digite 0 como valor de saque (condição de parada). """

valor = 1
valor_digitado = 1

while valor_digitado != 0:

    valor = int(input("Valor que deseja sacar: "))
    print(f"Valor: R${valor}")
    valor_digitado = valor


    notas50 = valor // 50
    valor = valor % 50

    notas20 = valor // 20
    valor = valor % 20

    notas10 = valor // 10
    valor = valor % 10

    notas5 = valor // 5
    valor = valor % 5

    nota = notas50, notas20, notas10, notas5

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
    
    if valor_digitado == 0:
        break

