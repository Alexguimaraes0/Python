import time

atividades = []
tempo_gasto = 0
escolha = ""


while True:
    print("Contador de Horas")

    print('=~' * 30)

    print("1 - Registrar atividade\n2 - Ver resumo do dia\n3- Escolher atividade\n0- Sair")

    if escolha == 1:
        atividade = input("Nome da Atividade: ")
        nome_numero = (atividade, 1)
        atividades.append(nome_numero)

    elif escolha == 2:
        if atividades == []:
            print("Nenhuma atividade registrada")
        if atividades != []:
            print(f"{atividades}-> 1")

    elif escolha == 3:
        print("Atividades registradas:")
        for indice, atividade in enumerate(atividades):
           print(f"{(indice + 1)} -> {atividade[0]}")
           

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
            print(f"{tempo:.2f}")

    escolha = int(input("oque deseja? "))
