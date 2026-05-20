""" Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é 
equilátero, isósceles ou escaleno. """

a = int(input('Digite o valor do primeiro lado:'))
b = int(input('Digite o valor do segundo lado:'))
c = int(input('Digite o valor do terceiro lado:'))

# Verifica se são válidos (positivos)
if a <= 0 or b <= 0 or c <= 0:
        print('Valores inválidos! Os lados devem ser maiores que 0.')
# Verifica se formam um triângulo (desigualdade triangular)
elif a + b <= c or a + c <= b or b + c <= a:
    print('Esses valores NÃO formam um triângulo válido!')
# Classifica o triângulo
if a == b and b == c:
    print('O triangulo é equilatero')
elif(a == b or b == c or a == c):
    print('O seu triangulo é isósceles')
else: 
    print('Seu triangulo é Escaleno')