notas = []


# repete 5 vezes, x vai de 0 a 4
for x in range(5):
    codigo_aluno = input('RM:')
    nota = float(input('Nota:'))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

# mostra quantas notas foram guardadas
print('Quantidades de notas', len(notas) )

# "n" ira percorrer a lista "notas"

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print('O RM', codigo_aluno, 'tirou a nota:', nota)