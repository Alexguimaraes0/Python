""" Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos. """


pessoas18 = 0
homens = 0
mulheres = 0

while True:
    print('-' * 20)
    print("      CADASTRO")
    print('-' * 20)

    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F] ").strip().upper()
    while sexo not in "mMfF":
        sexo = input("Sexo [M/F] ").strip().upper()
    if idade >= 18:
        pessoas18 += 1
    if sexo == "M":
        homens += 1
    elif sexo == "F":
        if idade < 20:
            mulheres += 1   
    continuar = input("Você quer Continuar? [S/N] ").strip().upper()
    while continuar not in "SsNn":
        continuar = input("Você quer Continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break
print('=' * 15, 'Fim do programa', '=' * 15)
print(f"Total de pessoas com mais de 18 anos: {pessoas18}")
print(f'Homens Cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres}')
