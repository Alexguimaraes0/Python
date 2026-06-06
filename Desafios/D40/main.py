#Crie um programa que faça o computador jogar Jokenpô com você.
import random

lista = ['pedra', 'papel', 'tesoura']

print('Jogue!')
eu = input('Jokenpô... ').lower()
maquina = random.choice(lista)
print(maquina)

if eu == 'papel' and maquina == 'pedra':
    print('Você ganhou!')
elif eu == 'tesoura' and maquina == 'papel':
    print('Você ganhou!')
elif eu == 'pedra' and maquina == 'tesoura':
    print('Você ganhou!!')
elif eu == maquina:
    print('Empate!')
else:
    print('Você perdeu!')