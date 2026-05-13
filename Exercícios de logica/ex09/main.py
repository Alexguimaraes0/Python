""" Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela 
sua condição 
de acordo com a tabela abaixo:

Fórmula do IMC = peso / (altura) ²

Tabela Condições IMC

 Abaixo de 18,5   | Abaixo do peso  

 Entre 18,6 e 24,9 | Peso ideal (parabéns)

 Entre 25,0 e 29,9 | Levemente acima do peso

 Entre 30,0 e 34,9 | Obesidade grau I 

 Entre 35,0 e 39,9 | Obesidade grau II (severa)

 Maior ou igual a 40 | Obesidade grau III (mórbida) """

peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura'))

imc = round((peso / pow(altura,2)),2)

if( imc < 18.5):
    print('tá mago filho')
    print('Seu Índice: {}'.format(imc,2))
elif(imc >= 18.6 or imc <= 24.9):
    print('Pense em um caba perfeito')
    print('Seu Índice: {}'.format(imc,2))
elif(imc >= 25.0 or imc <= 29.9):
    print('Tá mei gordin')
    print('Seu Índice: {}'.format(imc,2))
elif(imc >= 30.0 or imc <= 34.9):
    print('Meu fi tu tá caminhando pa uma lua')
    print('Seu Índice: {}'.format(imc,2))
elif(imc >= 35.0 or imc <= 39.9):
    print('Meu fi tá um satélite natural')
    print('Seu Índice: {}'.format(imc,2))
elif(imc >= 40):
    print('O caba quer competir com Júpiter')
    print('Seu Índice: {}'.format(imc,2))