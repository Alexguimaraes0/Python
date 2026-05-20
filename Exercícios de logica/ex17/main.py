"""  Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.]
Fórmula: C = (5 * ( F-32) / 9) """

cel = float(input('Digite a temperatura:'))
f = cel

cel = (5 * ( f-32) / 9)

print(f'convertendo da:{cel:.1f}')