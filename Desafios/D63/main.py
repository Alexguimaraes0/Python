""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo. """

num = int(input("Digite um número: "))
c = 0

while True:
    if num < 0:
        print("Números negativos são invalidos")
        break
    print(f'{num} X {c}')
    if c > 9 :
        num = int(input("Digite outro número: "))

        c = 0
        
    c += 1