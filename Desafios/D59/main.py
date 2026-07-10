""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). """

num = int(input("Digite um valor: "))
quant = 0
soma = num

while num != 999:
    num = int(input("Digite o próximo valor: "))
    quant += 1
    soma += num
print(f'Você digitou {quant} números.')
print(f'A soma entre eles tem o valor de: {soma}')