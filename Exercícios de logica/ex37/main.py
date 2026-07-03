"""Tenha uma lista com as notas de um aluno: notas = [7.5, 8.0, 6.5, 9.0, 5.5]
Use um for para percorrer a lista e:
Imprimir cada nota, indicando se ela é "Aprovado" (nota >= 6.0) ou "Reprovado" (nota < 6.0)
Somar todas as notas para calcular a média no final """

alunos = []
soma_alunos = 0

for c in range(1, 6):
    nota = float(input('Digite sua {}ª nota: '.format(c)))
    alunos.append(nota)
    soma_alunos += nota

for i in range(len(alunos)):
    nota = alunos[i]
    if nota >= 6:
        print(f'Nota {nota}: Aprovado')
    else:
        print(f'Nota {nota}: Reprovado')

media = soma_alunos / c
print(f'Média do Aluno: {media:.2f}')