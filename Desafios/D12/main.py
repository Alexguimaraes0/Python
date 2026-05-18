""" Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dia = int(input('Quantos dias ele foi alugado?:'))
km = int(input('Quantos Km você percorreu?:'))

valord = dia * 60
valorkm = km * 0.15

valor_total = valord + valorkm

print(f'O total a pagar é de R${valor_total:.2f}')
