#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO" 

cidade = input('Digite o Nome da sua Cidade:').strip()
print(cidade[:5].upper() == 'SANTO')