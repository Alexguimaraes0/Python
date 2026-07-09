#Refaça o DESAFIO 46, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

term = int(input('Digite o primeiro termo: '))
razao = int(input('Qual é a razão: '))
primeiro_termo = term
cont = 0

while cont < 10:
    print(primeiro_termo + cont * razao)
    cont += 1
