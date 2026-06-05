""" Crie um programa que cadastre vários alunos.Para cada aluno, peça:
Nome
Nota 1
Nota 2
No final, mostre:
A média de cada aluno.
O nome do aluno com a maior média.
O nome do aluno com a menor média.
A média geral da turma. """

quantidade_alunos = int(input('Quantos alunos iremos cadastrar: '))
contador = 0

nomes = []
medias = []

while contador < quantidade_alunos:
    contador += 1
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2

    nomes.append(nome)
    medias.append(media)

    print('-' * 10)


print('Média: ')
contador = 0
while contador < len(nomes):
    print(f'{nomes[contador]} -> {medias[contador]}')
    contador += 1

print('=' * 10)

maior_media = medias[0]
contador = 0

while contador < len(medias):
    
    if medias[contador] > maior_media:
        maior_media = medias[contador]
        contador +=1
print('Maior média: {}'.format(maior_media))
