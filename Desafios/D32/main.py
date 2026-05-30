#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRêS RETAS E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.
#A formação de um triângulo depende das 3 pontas seguirem essa função:
"""
A + B > C
A + C > B
B + C > A
As somas de 2 partes têm que ser maior que a 3°
"""

a = float(input('1ª Reta: '))
b = float(input('2ª Reta: '))
c = float(input('3ª Reta: '))

if a + b > c and a + c > b and b + c > a:
    print('Formar um triângulo é possível!')
else:
    print('Formar um triângulo NÃO é possível!')