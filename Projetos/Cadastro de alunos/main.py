
escolha = 1

while escolha != 0:
    print('=' * 10, 'MENU', '=' * 10)

    print("1 - Cadastrar Aluno")
    print("2 - Listar Alunos")  
    print("3 - Mostrar Média da turma")
    print("4 - Mostrar Aluno com a maior nota")
    print("0 - Sair")

    escolha = int(input("Qual opção deseja? "))

    alunos = []


    if escolha == 1:
        nome = input("Nome: ")
        nota = int(input("Nota: "))
        lista = [nome, nota]
        alunos.append(lista)
    print(alunos)

    if escolha == 2:
        