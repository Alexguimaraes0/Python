""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não ... """

lista = []

while True:
    num = int(input("Digite um número: "))
    lista.append(num)

    resp = input("Deseja continuar? [S/N]").strip().upper()
    while resp != "S" and resp != "N":
        resp = input("Deseja continuar? [S/N]").strip().upper()

        if resp == "N":
            print(f"Total de números adicionados:{len(lista)}")
            lista.sort(reverse=True)
            print(f"Lista em forma decrescente:{lista}")

            if 5 in lista:
                print("O valor 5 está adicionado a lista")
            else:
                print("O valor 5 Não está adicionado a lista")
        
            