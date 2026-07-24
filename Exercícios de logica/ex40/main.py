""" Crie um programa que leia uma frase digitada pelo usuário e conte quantas vogais
(a, e, i, o, u) ela contém, mostrando também quantas vezes cada vogal apareceu separadamente. """

total = 0
a = 0
e = 0
i = 0
o = 0
u = 0

frase = input("Digite uma frase: ")
c = 0
while c < len(frase):
    letra = frase[c].lower()

    if letra == 'a':
        a += 1
        total += 1

    if letra == 'e':
        e += 1
        total += 1

    if letra == 'i':
        i += 1
        total += 1

    if letra == 'o':
        o += 1
        total += 1

    if letra == 'u':
        u += 1
        total += 1

    c += 1

print(f"Total de vogais: {total}")
print(f'a: {a}')
print(f'e: {e}')
print(f'i: {i}')
print(f'o: {o}')
print(f'u: {u}')