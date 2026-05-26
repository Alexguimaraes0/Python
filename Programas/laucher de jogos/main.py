import os

while True:
    print('=' * 20)
    print('1 - Discord')
    print('2 - Steam')
    print('3 - LoL')
    print('4 - Navegador')

    escolha = int(input('Digite:'))

    if escolha == 1:
        os.startfile(r'C:\Users\alex0\AppData\Local\Discord\app-1.0.9238\Discord.exe')
    
    elif escolha == 2:
        os.startfile(r'C:\Program Files (x86)\Steam\steam.exe')

    elif escolha == 3:
        os.startfile(r'C:\Riot Games\League of Legends\Game\League of Legends.exe')

    elif escolha == 4:
        os.startfile(r'C:\Program Files\Zen Browser\zen.exe')

    else:
        print('Resposta invalida!')