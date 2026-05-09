""" Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, 
caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e
imprimir seu valor na tela. """

A = int(input("1° Número:"))
B = int(input("2° Número:"))

pombo = ""

def cavalo():

    if(A == B):
        pombo = (A + B, "São iguais")

    else:

        pombo = (A * B, "Não são iguais")

    return pombo

print(cavalo())