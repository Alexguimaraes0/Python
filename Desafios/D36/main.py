"""FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
SE ELE AINDA vai SE ALISTAR AO SERVIÇO MILITAR
SE É A HORA DE SE ALISTAR
SE JÁ PASSOU O TEMPO DE ALISTAMENTO
SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO
"""
import datetime

ano_nascimento = int(input('Em que ano você nasceu? '))

idade = datetime.datetime.now()

if (idade.year - ano_nascimento) < 18:
    print('Você ainda vai ter que se alistar.')
    print(f'Ainda falta {18 - (idade.year - ano_nascimento)} anos para se alistar')

elif (idade.year - ano_nascimento) == 18:
    print('Já está na hora de se alistar!')

elif (idade.year - ano_nascimento) > 18:
    print('Já passou da hora de você se alistar!')
    print(f'Já passou {(idade.year - ano_nascimento) - 18} anos para se alistar ')