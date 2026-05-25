#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O 
#COMPRIMENTO DA HIPOTENUSA
import math

num1 = float(input('Digite os cateto oposto:'))
num2 = float(input('Digite os cateto adjacente:'))

soma = math.hypot(num1, num2)

print('A hipotenusa vai medir:{:.2f}'.format(soma))