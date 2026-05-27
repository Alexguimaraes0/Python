""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza """

name = input('Enter your Name:')

divided = name.split()

print('First Name:',divided[0])
print('Last Name:',divided[-1])