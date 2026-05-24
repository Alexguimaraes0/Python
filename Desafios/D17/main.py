#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

alunos =    ['lucas', 'pablo', 'vinicius', 'carlos']
random.shuffle(alunos)

print('A ordem dos alunos será:')

# O enumerate começa a contar a partir do 1 (start=1)
for indice, aluno in enumerate(alunos, start=1):
    print(f"{indice}° {aluno.title()}")

print("===============================")