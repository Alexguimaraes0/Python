""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista na lista, ele não será adicionado.
No final, serão exibidos todos os valores digitados, em ordem crescente. """

numeros = []

while True:

    num = int(input("Digite um número: "))
    if num in numeros:
        print("Este número ja está adicionado a lista, item não contabilizado...")

    else:
        numeros.append(num)
        print("Valor adicionado com sucesso...")

    pergunta = input("Quer continuar? [S/N] ").strip().upper()


    if pergunta == "N":
        print(f'{sorted(numeros)}')
        break
