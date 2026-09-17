""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista na lista, ele não será adicionado.
No final, serão exibidos todos os valores digitados, em ordem crescente. """

numeros = 0

while True:

    num = int(input("Digite um número: "))
    numeros += num
    pergunta = input("Quer continuar? [S/N] ").split().upper()
    if pergunta == "N":
        print(sorted(numeros))