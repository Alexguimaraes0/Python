""" Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando-os de modo tabular. """

produtos = (("pão", 1.00), ("Leite", 5.50), ("Frango", 12.50), ("biscoito", 2.50), ("Água", 3), ("sorvete", 10.00), ("arroz", 4.50), ("feijão", 4), ("açucar", 3.40))

print('-' * 40)
print("           Listagem de preço")
print('-' * 40)

for nome, preco in produtos:
    print(f'{nome:.<20}R$ {preco:7.2f}')