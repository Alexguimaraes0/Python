#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. No final, mostre os 10 primeiros termos dessa progressão
""" an = a1(n - 1) * r """

term = int(input('Digite o primeiro termo: '))
razao = int(input('Qual é a razão: '))
primeiro_termo = term


for c in range(1,11):
    print(primeiro_termo + (c - 1) * razao)