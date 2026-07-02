#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPÁRES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500

sum = 0
cont = 0

for c in range(1,500,2):
    
    if c % 3 == 0:
        cont += 1
        sum += c
    print(c)

print('=' * 20)
print(f'A soma de todos os {cont} valores solicitados: {sum}')