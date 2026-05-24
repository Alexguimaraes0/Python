#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

num = float(input('Digite o angulo:'))
num = math.radians(num)

print(round(math.sin(num),2))
print(round(math.cos(num),2))
print(round(math.tan(num),2))