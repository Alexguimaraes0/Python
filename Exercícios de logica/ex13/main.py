""" Faça algoritmo que leia o nome e a idade de uma pessoa e imprima na tela o nome da pessoa e se ela é maior ou menor de idade.  """

nome = input('Qual é o seu nome?:')
idade = int(input('Quantos anos você tem?:'))

print(f'Nome:{nome}')

if idade >= 18:
    print('Ela é maior de idade')
else:
    print('Ela é de menor')