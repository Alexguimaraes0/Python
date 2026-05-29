#ESCREVA UM PROGRAM QUE LEIA A VELOCIDADE DE UM CARRO. SE ELA ULTRAPASSAR 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R% 7,00 por cada Km acima do limite

km = float(input('Quantos km: '))

if km > 80:
    print('Você foi multado!')
    multa = (km - 80) * 7
    print('Você terá que pagar R${} a mais'.format(multa))
else:
    print('Você estava na velocidade adequada, pode seguir!')