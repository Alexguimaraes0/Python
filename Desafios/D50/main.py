#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


pessoas = []

for c in range(5):
    peso = float(input('Digite seu peso: '))
    pessoas.append(peso)

print(max(pessoas))
print(min(pessoas))