""" Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento

 pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

 Tabela de Código de Condições de Pagamento

 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto

 2 - À Vista no cartão de crédito, recebe 10% de desconto

 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros

 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10% """

valor = float(input('Valor do produto:'))

print('1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto')
print('2 - À Vista no cartão de crédito, recebe 10% de desconto')
print( '3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros'
)
print( '4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%'
)

esco = int(input('Qual forma de pagamento:'))

if (esco == 1):
    print('O preço com o desconto aplicado:{:.2f}'.format(valor * 0.85))
    
elif esco == 2:
    print('O preço com o desconto aplicado:{:.2f}'.format(valor * 0.90))

elif esco == 3:
    print('O preço com o desconto aplicado:{:.2f}'.format(valor * 1/2))

elif esco == 4:
    print('O preço com o desconto aplicado:{:.2f}'.format(valor * 1.10))



