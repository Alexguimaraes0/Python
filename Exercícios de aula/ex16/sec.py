n = 1
r = ''
while n != 0:
    n = int(input('Digite um valor: '))
    if n == 0:
        r = input('Quer continuar? [S/N] ').upper()
    if r == 'N':
        print('Fim')
    if r == 'S':
        n = 1
        