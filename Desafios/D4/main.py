""" Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média """   
import time

bimestre1 = float(input('Nota do 1° Bimestre:'))
bimestre2 = float(input('Nota do 2° Bimestre:'))

soma = bimestre1 + bimestre2

time.sleep(0.5)

print('Sua Média:', soma / 2)

time.sleep(0.5)

total = soma / 2

if (total >= 7):
    print('Aprovado!!')
else:
    print('SEU FODIDO!!!')
