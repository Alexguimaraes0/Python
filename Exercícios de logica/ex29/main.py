""" Pergunte quantos produtos serão cadastrados.
Para cada produto, peça:
Nome
Preço

Ao final, mostre:

Quantos produtos foram cadastrados.
O nome do produto mais caro.
O nome do produto mais barato.
A média dos preços. """

num_produtos = int(input("Quantos produtos serão cadastrados? "))
nomes = []
precos = []
contador = 0

while contador < num_produtos:
    nome = input('Nome do Produto: ')
    preco = float(input('Preço do Produto: '))
    contador += 1

    nomes.append(nome)
    precos.append(preco)

print('-' * 10)

print(f'Números de Produtos cadastrados: {num_produtos}')

maior_preco = max(precos)
indice = precos.index(maior_preco)
nome_mais_caro = nomes[indice]

print(f'O produto {nome_mais_caro} tem o maior preço valendo: R${max(precos)}')

menor_preco = min(precos)
indice_menor = precos.index(menor_preco)
nome_mais_barato = nomes[indice_menor]

print(f'O produto {nome_mais_barato} tem o menor preço valendo R${min(precos)}')

media = sum(precos) / num_produtos
print(f'A média dos preços é R${media:.2f}')