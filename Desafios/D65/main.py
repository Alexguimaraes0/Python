""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato. """

produtos = []
soma = 0
mais1000 = 0
produto_barato = float('inf')
nome_produto_barato = ""

while True:
    print('=' * 20,"Loja", '=' * 20)

    produto = input("Produto: ")
    preco = int(input("R$"))
    produtos.append(produto)
    if preco < produto_barato:
        produto_barato = preco
        nome_produto_barato = produto
    if preco > 1000:
        mais1000 += 1
    soma += preco
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    while continuar not in "sSnN":
        continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break

print(f"Total Gasto na compra: {soma}")
print(f"Produtos acima de 1000R$: {mais1000}")
print(f"produto mais barato: {nome_produto_barato} custando {produto_barato}R$")
