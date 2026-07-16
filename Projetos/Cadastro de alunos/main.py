import time

escolha = 1
alunos = []
soma = 0
maior_nota = 0
maior_nota_nome = ""

while escolha != 0:
    print('=' * 10, 'MENU', '=' * 10)

    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")  
    print("3 - Mostrar Média da turma")
    print("4 - Mostrar Aluno com a maior nota")
    print("0 - Sair")

    escolha = int(input("Qual opção deseja? "))

    if escolha == 1:
        nome = input("Nome: ")
        nota = int(input("Nota: "))
        lista = [nome, nota]
        alunos.append(lista)    
        soma += nota
        if nota > maior_nota:
            maior_nota = nota
            maior_nota_nome = nome

    elif escolha == 2:
        if alunos == []:
            print("Nenhum aluno Cadastrado!")
        else:
            for numero, lista in enumerate(alunos, start=1):
                print(f'{numero} -> {lista[0]} -> {lista[1]}')


    elif escolha == 3:
        if alunos == []:
            print("Nenhum aluno Cadastrado!")
        else:
            media = soma / len(alunos)
            print(f'Média: {media:.2f}')


    elif escolha == 4:
        if alunos == []:
            print("Nenhum aluno Cadastrado!")
        else:
            print('Aluno com a maior nota: {} -> {}pts.'.format(maior_nota_nome, maior_nota))
    time.sleep(1)

    if escolha == 0:
        print('Fechando...')
        time.sleep(1)
        break

