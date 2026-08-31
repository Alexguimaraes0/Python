""" Desafio: Boletim da Turma

Dada uma turma (lista de tuplas no formato (nome, lista_de_notas)),
implementar três funções:

1. media_aluno(aluno) -> recebe (nome, notas) e retorna a média das notas.
2. lista_aprovados(turma) -> retorna os nomes dos alunos com média >= 6.0.
3. melhor_aluno(turma) -> retorna a tupla (nome, notas) do aluno com maior média.

Reaproveitar media_aluno() nas outras funções. Lista de notas tem tamanho
variável. Imprimir aprovados e o melhor aluno com média formatada (2 casas). """

alunos = []
notas = []
cont = 0

while cont < 4:

    nome = input("Insira o nome do aluno(a): ")
    nota1 = float(input("Insira a nota do aluno(a): "))
    nota2 = float(input("Insira a nota do aluno(a): "))
    nota3 = float(input("Insira a nota do aluno(a): "))
    print('-' * 30)
    notas = nota1, nota2, nota3
    notageral = nome, notas
    alunos.append(notageral)

    cont += 1

def media_aluno(aluno):
        nome, notas = aluno
        return sum(notas) / len(notas)

def lista_aprovados(turma):
      return [nome for nome, notas in turma if media_aluno((nome, notas)) >=6]

def melhor_aluno(turma):
      return max(turma, key=media_aluno)

aprovados = lista_aprovados(alunos)
melhor = melhor_aluno(alunos)

print(f"aprovados: {aprovados}")
print(f"Melhor aluno: {melhor[0]} - Média: {media_aluno(melhor):.2f}")

