""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições no lista. """

valor1 = int(input("Digite o 1º valor: "))
valor2 = int(input("Digite o 2º valor: "))
valor3 = int(input("Digite o 3º valor: "))
valor4 = int(input("Digite o 4º valor: "))
valor5 = int(input("Digite o 5º valor: "))

valor_total = [valor1, valor2, valor3, valor4, valor5]

print('-=' * 30)

print(f"Você digitou os valores:", *valor_total)

valor_max = max(valor_total)
valor_min = min(valor_total)

print(f"O maior valor foi o {valor_max} na posição {valor_total.index(valor_max) + 1}")
print(f"O menor valor foi o {valor_min} na posição {valor_total.index(valor_min) + 1}")