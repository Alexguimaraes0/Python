""" Crie um programa que:

Pergunte quantos alunos serão cadastrados.
Para cada aluno, peça apenas o nome.

Ao final, mostre:
Quantos alunos foram cadastrados.
O primeiro aluno cadastrado.
O último aluno cadastrado.
A lista completa de alunos. """

quantidade_alunos = int(input('Quantos alunos serão cadastrados: '))
contador = 0
alunos = []
while contador < quantidade_alunos:
    nome = input('Nome: ')
    alunos.append(nome)
    contador += 1
print('-' * 10)

print(f'Quantidade de alunos cadastrados: {quantidade_alunos}')
print(f'Primeiro aluno cadastrado: {alunos[0]}')
print(f'Ultimo aluno cadastrado: {alunos[-1]}')

print('-' * 10)

print('lista de Alunos:')
for aluno in alunos:
    print(aluno)
