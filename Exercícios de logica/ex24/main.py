# CRIE UM PROGRAMA QUE CADASTRE ALUNOS E SUAS NOTAS.
#
# 1. PERGUNTAR QUANTOS ALUNOS SERÃO CADASTRADOS.
# 2. SOLICITAR O NOME E A NOTA DE CADA ALUNO.
# 3. ARMAZENAR OS DADOS EM UMA LISTA.
# 4. AO FINAL, MOSTRAR:
#    - A QUANTIDADE DE ALUNOS CADASTRADOS.
#    - A MÉDIA DAS NOTAS DA TURMA.
#    - O NOME E A NOTA DO ALUNO COM A MAIOR NOTA.
#    - O NOME E A NOTA DO ALUNO COM A MENOR NOTA.

quantidade_alunos = int(input('Quantos alunos serão cadastrados? '))

contador = 1

alunos = []
soma_notas = 0

while contador <= quantidade_alunos:
    nome = input('Nome: ')
    nota = float(input('Nota: '))

    aluno = [nome, nota]
    alunos.append(aluno)

    soma_notas += nota

    if contador == 1:
        maior_nota = nota
        menor_nota = nota
        maior_nome = nome
        menor_nome = nome
    else:
        if nota > maior_nota:
            maior_nota = nota
            maior_nome = nome

        if nota < menor_nota:
            menor_nota = nota
            menor_nome = nome

    contador += 1

print(alunos)

print('=' * 20)

print('Cadastros: {}'.format(quantidade_alunos))
print('Média: {:.2f}'.format(soma_notas / quantidade_alunos))
print('O aluno com a maior nota {} tirou {:.1f}'.format(maior_nome, maior_nota))
print('O aluno com a menor nota {} tirou {:.1f}'.format(menor_nome, menor_nota))