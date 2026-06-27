""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos. """

soma_idade = 0
homem_velho = ''
maior_idade = 0
contador_mulher = 0
quantidade = 4

for c in range(quantidade):
    nome = input('Digite seu Nome: ')
    idade = int(input('Digite sua Idade: '))
    sexo = input('Digite seu gênero: ').strip.lower()
    soma_idade += idade
    if sexo == 'homem':
        if idade > maior_idade:
            maior_idade = idade
            homem_velho = nome
    if sexo == 'mulher':
        if idade < 20:
            contador_mulher += 1

media = soma_idade / quantidade 
print(f'{media} é a média de idades do grupo')

if homem_velho == '':
    print('Não existe homens no grupo')
else:

    print(f'O {homem_velho} é o homem mais velho com {maior_idade} anos ')

print(f'Existem {contador_mulher} Mulheres abaixo de 20 anos')
