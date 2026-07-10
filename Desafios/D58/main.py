""" Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex:
0 → 1 → 1 → 2 → 3 → 5 → 8 """

n = int(input("Digite um valor: "))
cont = 0
anterior = 0
atual = 1

while cont < n:
    print(f'{anterior} -> ', end="")
    valor = anterior + atual
    anterior = atual
    atual = valor
    cont += 1