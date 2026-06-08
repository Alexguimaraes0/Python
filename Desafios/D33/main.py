"""  Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
 O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. """

house = float(input('Qual o valor da casa que você deseja comprar? '))
salary = float(input('Qual o seu salário? '))
years = int(input('Em quantos anos você vai pagar? '))

months = years * 12
installment = house / months
limit = salary * 0.30   

print('Para pagar uma casa de R${:.2f} em {} anos '.format(house, years), end='')
print(' a prestração sera de R${:.2f} anos'.format(installment))

if installment > limit:
    print('Emprestimo Negado!')
else:
    print('Emprestimo Aprovado!')