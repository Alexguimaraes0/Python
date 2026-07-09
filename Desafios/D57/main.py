#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

term1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 0

while cont < 10:
    print(term1 + cont * razao)
    cont += 1


termos = int(input('Quantos termos vc deseja a mais? '))

if termos == 0:
    print('Fim!')

while termos > 0 :
    while cont < 10:
        print((term1 + termos) + cont * razao)
    
    termos = int(input('Quantos termos vc deseja a mais? '))
    cont += 1