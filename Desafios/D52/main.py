#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

r = ''
while r != "M" or "F":
    r = input('Digite "M" para (masculino) "F" para (feminino): ').upper()
    if r == 'M':
        print('Sexo: Masculino')
        break
    if r == 'F':
        print('Sexo: Feminino')
        break