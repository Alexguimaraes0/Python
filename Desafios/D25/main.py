#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 4 E 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO
import random

num = random.randint(4, 5)
adv = int(input('Guess a number beetween 4 and 5:'))

if adv == num:
    print('You got it right!!')
else:
    print('You lose!')
print(adv)