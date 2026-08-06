# Controle de estoque - Loja de conveniência
# Cada produto: código, preço, descrição, disponibilidade
# Funcionalidades: cadastro, consulta e atualização de estoque

produtos = []

while True:
    codigo = int(input("Código do produto: "))
    preco = float(input("Preço do produto: R$"))
    descricao = input("Nome: ")
    disponibilidade = (input("Disponibilidade [S/N]: ")).strip().upper()
    disponivel = True if disponibilidade == "S" else False

    produto = codigo, preco, descricao, disponivel

    produtos.append(produto)

    print("_" * 20)

    dnv = input("Deseja continuar? [S/N]").strip().upper()

    if dnv == "N":
        print("=~" * 20)

        vizual = input("Deseja Vizualizar o estoque? [S/N]: ").strip().upper()
        if vizual == "S":
            for pos, produto in enumerate(produtos):
                print(f"{pos + 1} -> {produto[2]}")

            escolha = int(input("Qual produto deseja ver? "))

            if 1 <= escolha <= len(produtos):
                    produto_escolhido = produtos[escolha - 1]
                    status = "Sim" if produto_escolhido[3] else "Não"
                    print(f"Produto: {produto_escolhido[2]}\n Código: {produto_escolhido[0]}\n Preço: {produto_escolhido[1]}\n Disponibilidade: {status}")

            else:
                    print("Produto Invalido!")
        break