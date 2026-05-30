#ESCREVA UM PRORGRAMA QUE PERGUNTE O SALÁRIO ED UM FUNCIONÁRIO E CALCULE O VALOR DO SEU AUMENTO.
#PARA SALÁRIOS SUPERIORES A R$1.250,00 , CALCULE UM AUMENTO DE 10%.
#PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%

sal = float(input('Qual o seu sálario:').replace('.', ''))
aumento = sal * 0.1
aumento15 = sal * 0.15


if sal >= 1250:
    print('Com o Aumento de 10%:R${}'.format(aumento + sal))

else:
    print('Com o Aumento de 15%:R${}'.format(aumento15 + sal))