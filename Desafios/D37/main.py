#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA
""" 
=MÉDIA ABAIXO DE 5.0: REPROVADO

=MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO

=MÉDIA 7.0 OU SUPERIOR: APROVADO
"""
import os

nota1 = float(input('Nota do 1° Bimestre: '))
nota2 = float(input('Nota do 2° Bimestre: '))

media = (nota1 + nota2) / 2

os.system('cls')

if media < 5:
    print('\033[4;31mReprovado!')
elif media > 5 and media < 7:
    print('\033[4;33mRecuperação!')
elif media > 7:
    print('\033[4;32mAprovado!')