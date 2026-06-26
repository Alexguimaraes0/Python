#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
atual = datetime.datetime.now()
pessoas = []
pessoasa = 0
pessoasb = 0

for c in range(7):
    pessoa = int(input('Ano de Nascimento: '))
    idade = atual.year - pessoa
    pessoas.append(idade)

for c in range(len(pessoas)):
    if pessoas[c] >= 18:
        pessoasa += 1
    else:
        pessoasb += 1
print('{} são maiores de idade.'.format(pessoasa))
print('{} são menores de idade.'.format(pessoasb))
