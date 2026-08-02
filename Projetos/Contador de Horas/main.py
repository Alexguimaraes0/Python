import time

atividades = []
tempo_gasto = 0
escolha = ""


while True:
    print("Contador de Horas")

    print('=~' * 30)

    print("1 - Registrar atividade\n2 - Ver resumo do dia\n0- Sair")

    if escolha == 1:
        atividade = input("Nome da Atividade: ")
        atividades.append(atividade)

    elif escolha == 2:
        if atividades == []:
            print("Nenhuma atividade registrada")
        if atividades != []:
            print(f"{atividades}-> 1")

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
            print(tempo)

    escolha = int(input("oque deseja? "))
