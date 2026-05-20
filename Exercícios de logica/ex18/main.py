""" Francisco tem 1,10m e cresce 3 centímetros por ano, enquanto Sara tem 1,50m e cresce 2 centímetros por ano.
 Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Francisco seja maior que Sara. """

francisco = 110 #cm
sara = 150 #cm
franciscocm = 3
saracm = 2
anos = 0

while francisco <= sara:
    francisco += franciscocm
    sara += saracm
    anos += 1

print(f'francisco ficara maior em {anos} anos')