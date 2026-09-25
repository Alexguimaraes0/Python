""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela. """


lista = []

for c in range(5):
    num = int(input("Digite um número: "))

    pos = 0
    while pos < len(lista) and lista[pos] < num:
        pos += 1

    lista.insert(pos, num)
    print(f"Adicionado na posição {pos} da lista...")

print(lista)