""" Melhore o jogo do DESAFIO 25 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
 mostrando no final quantos palpites foram necessários para vencer. """

import random

num = random.randint(0, 10)
adv = int(input("Guess a Number: "))
cont = 0

while adv != num:
    adv = int(input("Guess a Number: "))
    cont += 1
    if adv == num:
        print('You got it right')

print("You tried {} times until you got it right.".format(cont))