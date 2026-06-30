
alunos = []
nome_maior_nota = ''
maior_nota = 0
soma_nota = 0
contador7 = 0

for c in range(5):
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    alunos.append(nome)
    soma_nota += nota
    if nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome
    if nota >= 7:
        contador7 += 1

media = soma_nota / 5
print(f'A média ta turma é de: {media}')

print(f'O aluno com a maior nota é {nome_maior_nota} com {maior_nota} pontos.')

print(f'{contador7} alunos tiraram 7 ou mais.')

print(f'O primeiro aluno cadastrado: {alunos[0]}')