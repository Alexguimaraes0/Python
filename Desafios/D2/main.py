num = int(input('Digite um número:'))

sucessor = num
antecessor = num

print('Seu número:{}'.format(num))

while (sucessor < 10 and antecessor > 0):
    sucessor = sucessor + 1
    antecessor = antecessor - 1

    print('='*10)
    print('Número Sucessor {}'.format(sucessor))
    print('Número antecessor {}'.format(antecessor))
    print('='*10)

    if sucessor == 10 and antecessor == 0:

        print('='*10)
        print('Número Sucessor {}'.format(sucessor))
        print('Número antecessor {}'.format(antecessor))
        print('='*10)
        break

