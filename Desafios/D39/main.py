""" Refaça o DESAFIO 032 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes """


a = float(input('1ª Reta: '))
b = float(input('2ª Reta: '))
c = float(input('3ª Reta: '))

if a + b > c and a + c > b and b + c > a:
    print('Formar um triângulo é possível!')
else:
    print('Formar um triângulo NÃO é possível!')

if a == b == c:
    print('Equilátero')
elif a == b or b == c or a == c:
    print('Isósceles')
elif a != b and b != c and c != a:
    print('Escaleno')