#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA

num = int(input('Que número você deseja saber?:'))
t = 0

while (t != 10):
    t = t + 1

    print('{} X {} = {}'.format(num, t, num * t))