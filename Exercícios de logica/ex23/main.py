"""  
Faça um algoritmo que calcule a distância percorrida e a quantidade de litros de combustível gastos em uma viagem.
Sabendo que o carro faz 12km com um litro.

ENTRADA:
- Tempo da viagem (em horas)
- Velocidade média (em km/h)

SAÍDA:
- Distância percorrida (em km)
- Quantidade de litros utilizados

FÓRMULAS:
- distância = tempo × velocidade
- litros usados = distância ÷ 12
"""

tempo = float(input('Tempo de viagem em (horas):'))
velocidade = float(input('Quando km/h:'))

distancia = tempo * velocidade
litros = distancia / 12

print(f'Distancia percorrida (em km):{distancia}')
print(f'Quantidade de litros utilizados:{litros:.2f}')