"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares. """

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
num4 = int(input("Digite o ultimo número: "))

numeros = num1, num2, num3, num4

print(f"O valor 9 apareceu {numeros.count(9)} vez(es).")

if 3 in numeros:
    print(f"O valor 3 foi digitado na posição {numeros.index(3) + 1}.")
else:
    print("O valor 3 não foi digitado.")

print("Números pares:", end=" ")
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=" ")
print()