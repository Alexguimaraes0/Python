import time

atividades = []
atividade_atual = []
tempo_gasto = 0
escolha = ""


while True:

    if atividades == []:

        atividade = input("Registre sua primeira atividade: ")
        atividade_atual = atividade
        atividades.append(atividade)
        time.sleep(0.3)


        print("1 - Registrar atividades\n2 - Ver resumo do dia\n3 - Escolher atividade\n0 - Sair")


    else:

        escolha = int(input("oque deseja? "))

        if escolha == 1: 
            atividade = input("Nome da Atividade: ")
            atividades.append(atividade)
            atividade_atual = atividade

        elif escolha == 2:
            if atividades == []:
                print("Nenhuma atividade registrada")
            if atividades != []:
                for atividade in atividades:
                    print(f"{atividade} -> {atv_tempo[1]}")

        elif escolha == 3:
            if atividades == []:
                print("Nenhuma atividade registrada")
            print("Atividades registradas:")
            for indice, atividade in enumerate(atividades):
                print(f"{(indice + 1)} -> {atividade}")
            atv = int(input("Qual Atividade deseja? "))
            atv -= 1
            atv = atividades[atv]
            atividade_atual = atv
            
            
        elif escolha == 0:
            print("Encerrando...")
            time.sleep(1)
            break

        print('=~' * 30)
        
        if atividades != []:
            print("Para inicar contagem pressione 4 ")
            if escolha == 4:
                start = input("Aperte ENTER para começar...")

                inicio = time.time()
                end = input("Pressione Enter quando terminar...")
                fim = time.time()
                tempo = fim - inicio
                atv_tempo = atividade_atual, tempo
