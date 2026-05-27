#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = input('Digite seu Nome:')

print('Seu nome tem Silva? {}'.format('silva' in name.lower()))
