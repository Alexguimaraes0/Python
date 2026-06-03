""" Faça um programa que leia o nome de um aluno e duas notas.

Depois mostre:

O nome do aluno.
A média das duas notas.
Se a média for maior ou igual a 7, mostre "Aprovado".
Caso contrário, mostre "Reprovado". """

name = input('Enter your name: ')
school_grade1 = int(input('Enter your school grade 1: '))
school_grade2 = int(input('Enter your school grade 2: '))

print(f'Name: {name}')
print(f'School Grade 1: {school_grade1}')
print(f'School Grade 2: {school_grade2}')

print('-' * 10)

avarage = (school_grade1 + school_grade2) / 2
print(f'Aluno: {name}')
print(f'Avarage: {avarage}')


if avarage >= 7:
    print('Approved')
else:
    print('Failed')