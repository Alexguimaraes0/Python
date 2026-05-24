#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
import random

alunos = ['lucas', 'pablo', 'vinicius', 'carlos']

escolhido = random.choice(alunos)

print(f'Quem vai apagar o quadro é o {escolhido}')
