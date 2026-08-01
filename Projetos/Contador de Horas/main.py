import time

atividades = []

while True:

    print("1 - Registrar atividade\n2 - Ver resumo do dia\n0- Sair")
    escolha = int(input("oque deseja? "))
    if escolha == 1:
        atividade = input("Nome da Atividade: ")
        atividades.append(atividade)
    elif escolha == 2:
        if atividades == []:
            print("Nenhuma atividade registrada")
        print(atividades)
    elif escolha == 0:
        print("Encerrando...")
        time.sleep(1)
        break
