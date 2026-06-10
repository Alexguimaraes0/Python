#Faça um programa que peça um número inteiro ao usuário e mostre na tela todos os números de 1 até esse número, um por linha.

num = int(input('Digite um número: '))

for c in range(1, num+1):
    print(c)