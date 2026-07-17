""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
 que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag e usando o BREAK) . """

n = 0
s = 0
cont = 0

while True:
    n = int(input("Digite um número (999 para parar): "))
    if n == 999:
        break
    s += n
    cont += 1
print(f"Foram Digitados {cont} números e a soma equivale a {s}")