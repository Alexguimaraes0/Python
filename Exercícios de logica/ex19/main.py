"""  Faça um algoritmo que imprima na tela a tabuada de 1 até 10. """

num = 1

while num <= 10:
    mult = 1
    while mult <= 10:
        print(f'{num} X {mult} = {num * mult}')
        mult += 1
    print('=' * 12)
