""" Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """
from random import randint

print('=' * 20)
print("Par ou Impar?")
print('=' * 20)

partidas = 0
partidas_ganhas = 0
vitorias = 0
maior_vitorias = 0

while True:
    num = int(input("Digite um número: "))
    par_impar = input(("Par ou Impar [P/I]: ")).strip().upper()
    print('-' * 20)

    aleatorio = randint(1, 10)
    soma = num + aleatorio

    if (soma % 2) == 0:
        resultado = "P"
        resultado_texto = "Par"
    else:
        resultado = "I"
        resultado_texto = "Impar"

    print(f'Você jogou {num} e o computador jogou {aleatorio}. Total de {soma} Deu {resultado_texto}')
    print('-' * 20)
    partidas += 1

    if par_impar == resultado:
        print("Você Venceu!")
        vitorias += 1
        partidas_ganhas += 1
    else:
        print("Você perdeu")
        print(f"Vitorias consecutivas: {vitorias}")
        historico = int(input("Digite 1 para ver seu historico: "))
        if historico == 1:
            print("-" * 20)
            print(f"Partidas jogadas: {partidas} \nPartidas vencidas: {partidas_ganhas}")
        if vitorias > maior_vitorias:
            maior_vitorias = vitorias
            print("Parabens você atingiu seu record!")
        break
