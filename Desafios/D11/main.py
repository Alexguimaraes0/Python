#ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM °C E CONVERTA PARA °F

cel = float(input('Digite a temperatura em °C:'))
fah = cel * 1.8 + 32

print(f'{cel:.1f}°C convertido para °f são:{fah:.1f}°f')