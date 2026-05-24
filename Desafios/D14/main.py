#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O 
#COMPRIMENTO DA HIPOTENUSA
import math

num1 = float(input('Digite os catetos'))
num2 = float(input('Digite os catetos'))

soma = math.hypot(num1, num2)

print(math.trunc(soma))