""" Crie um programa que valide um número de telefone brasileiro digitado pelo usuário. O telefone deve seguir o formato (XX) XXXXX-XXXX
(com DDD de 2 dígitos, 5 dígitos, hífen, e mais 4 dígitos). O programa deve verificar se o formato está correto
(parênteses, espaço, hífen nas posições certas, e se as posições dos dígitos realmente são números) e informar se é válido ou não.
Repita até o usuário digitar um telefone válido. """


while True:

    telefone = input("Digite seu número: ")

    if len(telefone) == 15:

        if (telefone[0] == '(' and telefone[3] == ')' and telefone[4] == ' ' and telefone[10] == '-'
    and telefone[1].isdigit() and telefone[2].isdigit()
    and telefone[5].isdigit() and telefone[6].isdigit() and telefone[7].isdigit()
    and telefone[8].isdigit() and telefone[9].isdigit()
    and telefone[11].isdigit() and telefone[12].isdigit()
    and telefone[13].isdigit() and telefone[14].isdigit()):
            print("Número Validado!")
            break
        else: 
            print("Número Invalido!")
            print("Tente novamente.")
    else:
        print("Quantidade de números invalidas.")