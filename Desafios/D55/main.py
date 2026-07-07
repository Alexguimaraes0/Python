""" Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120 """

num = int(input("Digite um número: "))
fatorial = 1
i = 1
numeros = []

while i <= num:
    fatorial = fatorial * i
    numeros.append(i)
    i += 1

numeros.reverse()
print(f'{num}! = {"x".join(str(n) for n in numeros)} = {fatorial}')