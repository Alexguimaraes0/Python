#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
contador = 0
for num in range(1,7):
    sum = int(input('Digite um número: '))

    if (sum % 2) == 0:
        contador += sum
print(contador)