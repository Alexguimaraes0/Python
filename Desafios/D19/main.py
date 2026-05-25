#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# NOME COM TODAS AS LETRAS MAIÚSCULAS ✔️
# NOME COM TODAS MINÚSCULAS ✔️
# QUANTAS LETRAS AO TODO (SEM CONSIDERAR O ESPAÇO)
# QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = input('Digite seu nome:')
nome1 = nome.split()

print(nome.upper())

print(nome.lower())

print(len(nome.replace(' ', '')))

print(len(nome1[0]))