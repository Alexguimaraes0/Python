""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SÊNIOR
Acima de 20 anos: MASTER """
from datetime import date

ano_nascimento = int(input('Em que ano você nasceu? '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'O atleta tem {idade} anos.')

if idade < 9:
    print('Atleta Mirim!')
if idade <= 14:
    print('Atleta Infantil!')
if idade <= 19:
    print('Atleta Junior!')
if idade == 20:
    print('Atleta Sênior!')
if idade > 20:
    print('Atleta Master!')