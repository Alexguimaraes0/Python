""" Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 
 se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7. """

name = input('Seu Nome:')

print("======================================NOTA======================================")

luffy = float(input('1º Bimestre'))
zoro = float(input('2º Bimestre'))
sanji = float(input('3º Bimestre'))
jimbe = float(input('4º Bimestre'))

mul = luffy + zoro + sanji + jimbe / 3

print (round(mul,1))

if (mul > 7):
    print('Parabens {}! Você foi APROVADO!!'.format(name))
else:
    print('Infelizmente {}, Você foi REPROVADO!!'.format(name))
