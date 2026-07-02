#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time

exploda = input('aperte "ENTER" para começar os fogos: ')

for c in range(10, 0, -1):
    time.sleep(0.9)
    print(c)
    time.sleep(0.5)
print('FOGOS!!!!')