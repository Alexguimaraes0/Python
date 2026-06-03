import os 
import emoji
import time
import winsound

os.system('cls') 

print('=' * 20)
print('-Meu Menu-')

def abrir_discord():
    winsound.PlaySound(
    'discord-notification.wav',
    winsound.SND_FILENAME
)
    os.startfile(r'C:\Users\alex0\AppData\Local\Discord\app-1.0.9239\Discord.exe')

def abrir_steam():
    os.startfile(r'C:\Program Files (x86)\Steam\steam.exe')

def abrir_lol():
    os.startfile(r'C:\Riot Games\League of Legends\Game\League of Legends.exe')

def abrir_navegador():
    os.startfile(r'C:\Program Files\Zen Browser\zen.exe')


while True:

    print('=' * 20)
    print('1 - Discord 💬')
    print('2 - Steam 🎮')
    print('3 - LoL ⚔️')
    print('4 - Navegador 🌐')
    print('0 - Sair ❌')

    escolha = int(input('Escolha:'))

    if escolha == 1:
        abrir_discord()
    
    elif escolha == 2:
        abrir_steam()

    elif escolha == 3:
        abrir_lol()

    elif escolha == 4:
        abrir_navegador()

    elif escolha == 0:
        print('Fechando o Laucher...')
        time.sleep(0.8)
        break
            
    else:
        print('Resposta invalida!')

        