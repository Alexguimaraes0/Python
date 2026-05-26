import os 
import emoji
import time

os.system('cls')

print('=' * 20)
print('-Meu Menu-')

while True:

    print('=' * 20)
    print('1 - Discord 💬')
    print('2 - Steam 🎮')
    print('3 - LoL ⚔️')
    print('4 - Navegador 🌐')
    print('0 - Sair ❌')

    escolha = int(input('Escolha:'))

    if escolha == 1:
        os.startfile(r'C:\Users\alex0\AppData\Local\Discord\app-1.0.9238\Discord.exe')
    
    elif escolha == 2:
        os.startfile(r'C:\Program Files (x86)\Steam\steam.exe')

    elif escolha == 3:
        os.startfile(r'C:\Riot Games\League of Legends\Game\League of Legends.exe')

    elif escolha == 4:
        os.startfile(r'C:\Program Files\Zen Browser\zen.exe')

    elif escolha == 0:
        print('Fechando o Laucher...')
        time.sleep(0.8)
        break
            
    else:
        print('Resposta invalida!')